from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask.helpers import get_flashed_messages
from flask_session import Session
from helpers import apology, login_required, lookup, usd
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import os

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
   raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    stockInfo = db.execute(
        "SELECT userID, SUM(shares) as shares, operation FROM users WHERE userID = ? GROUP BY users HAVING (SUM(shares)) > 0;",
        session["user_id"],
    )
    totalStocks = 0
    for stockValue in stockInfo:
        quotes = lookup(stock["symbol"])
        stockValue["name"] = quotes["name"]
        stockValue["price"] = quotes["price"]
        stockValue["total"] = stockValue["price"] * stockValue["shares"]
        totalStocks = totalStocks + totalStock["total"]

    cashAmount = totalStocks + cash[0]["cash"]
    return render_template(
        "index.html", stockInfo=stockInfo, cash=cash[0], cashAmount=cashAmount
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        dollarSymbol = request.form.get("symbol")
        stockPrice = lookup(dollarSymbol)
        numShares = request.form.get("shares")
        cash = db.execute("SELECT cash FROM users WHERE id = ? ", session["user_id"])[0]["cash"]

        if not dollarSymbol:
            return apology("a valid symbol must be provide", 400)
        elif stockPrice is None:
            return apology("must provide valid symbol", 400)

        try:
            numShares = int(numShares)
            if numShares < 1:
                return apology("share must be a positive integer", 400)
        except ValueError:
            return apology("share must be a positive integer", 400)

        sharePrice = numShares * stockPrice["price"]
        if cash < (sharePrice):
            return apology("cash is not sufficient", 400)
        else:
            db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", sharePrice, session["user_id"],
            )
            db.execute( "INSERT INTO users (userID, symbol, shares, price, operation) VALUES (?, ?, ?, ?, ?)", session["user_id"], dollarSymbol.upper(),shares, price["price"], "buy",
            )

            flash("Transaction successful")
            return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    stockInfo = db.execute("SELECT * FROM stocks WHERE userID = ?", session["user_id"])
    return render_template("history.html", stockInfo=stockInfo)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        userInformation = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(userInformation) != 1 or not check_password_hash(
            userInformation[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = userInformation[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        quotes = lookup(request.form.get("symbol"))
        # Ensure the simbol was submitted
        if quotes is None:
            return apology("must provide valid symbol", 400)
        else:
            return render_template(
                "quoted.html",
                userName=quotes["name"],
                dollarSymbol=quotes["symbol"],
                stockPrice=quotes["price"],
            )
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        userName = request.form.get("username")
        passWord = request.form.get("password")
        confirm = request.form.get("confirmation")

        index = db.execute("SELECT * FROM users WHERE username = ?", userName)

        # Ensure the username was submitted
        if not userName:
            return apology("must provide username", 400)
        # Ensure the username doesn't exists
        elif len(index) != 0:
            return apology("username already exists", 400)

        # Ensure password was submitted
        elif not passWord:
            return apology("must provide password", 400)

        # Ensure confirmation password was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide a confirmation password", 400)

        # Ensure passwords match
        elif not passWord == confirm:
            return apology("passwords must match", 400)

        else:
            # Generate the hash of the password
            hashCode = generate_password_hash(
                passWord, method="pbkdf2:sha256", salt_length=8
            )
            # Insert the new user
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?) ", userName, hashCode,
            )
            # Redirect user to home page
            return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        dollarSymbol = request.form.get("symbol")
        numShares = request.form.get("shares")
        try:
            numShares = int(shares)
            if numShares < 1:
                return apology("shares must be a positive integer")
        except ValueError:
            return apology("shares must be a positive integer")
        if not dollarSymbol:
            return apology("missing symbol")

        stockPrice = db.execute(
            "SELECT SUM(shares) as shares FROM stocks WHERE userID = ? AND symbol = ?;",
            session["user_id"],
            symbol,
        )[0]

        if numShares > stockPrice["shares"]:
            return apology("You don't have this number of shares")
        stockPrice = lookup(dollarSymbol)["price"]
        shareValue = stockPrice * numShares

        db.execute(
            "INSERT INTO stocks (userID, symbol, shares, price, operation) VALUES (?, ?, ?, ?, ?)",
            session["user_id"],
            symbol.upper(),
            -numShares,
            stockPrice,
            "sell",
        )

        db.execute(
            "UPDATE users SET cash = cash + ? WHERE id = ?",
            shareValue,
            session["user_id"],
        )

        flash("Sold!")
        return redirect("/")
    else:
        stockInfo = db.execute(
            "SELECT symbol FROM stocks WHERE userID = ? GROUP BY symbol",
            session["user_id"],
        )
        return render_template("sell.html", stockInfo=stockInfo)


def errorhandler(error):
    """Handle error"""
    if not isinstance(error, HTTPException):
        error = InternalServerError()
    return apology(error.name, error.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)