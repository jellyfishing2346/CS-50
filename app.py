import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from helpers import apology, login_required, lookup, usd
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from passlib.apps import custom_app_context as pwd_context

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
    rowInfo = db.execute(
        "SELECT symbol, SUM(shares) FROM transactions WHERE user_id=:user_id GROUP BY symbol HAVING SUM(shares) > 0", user_id=session["user_id"])

    # Creates a holder to store all information of the user's finance details
    placeHolder = []
    total = 0

    for index in rowInfo:
        stockValue = lookup(row['symbol'])
        sums = (stockValue["price"] * index["SUM(shares)"])
        placeHolder.append({"symbol": stockValue["symbol"], "name": stockValue["name"],
                            "shares": index["SUM(shares)"], "price": usd(stockValue["price"]), "total": usd(sums)})
        total += stockValue["price"] * index["SUM(shares)"]

    rowInfo = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=session["user_id"])
    cashAmount = rowIngo[0]["cash"]
    total += cashAmount

    return render_template("index.html", placeHolder=placeHolder, cashAmount=usd(cashAmount), total=usd(total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST through sumbission via POST
    if request.method == "POST":

        # Make sure stock is sumbitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)

        # Make sure the shares are submitted
        elif not request.form.get("shares"):
            return apology("must provide shares", 403)

        # Make sure that theshares is greater than 0
        elif int(request.form.get("shares")) < 0:
            return apology("must provide a valid number of shares", 403)

        # Make sure that the symbol is valid
        if not request.form.get("symbol"):
            return apology("must provide an existing symbol", 403)

        # Analyze the stock value and the dollar sign
        dollarSymbol = request.form.get("symbol").upper()
        stockValue = lookup(dollarSymbol)

        # Determine the transaction value
        numShares = int(request.form.get("shares"))
        transactionInfo = numShares * stockValue['price']

        # Check if user has sufficient cash amount for transaction
        userCash = db.execute("SELECT cash FROM users WHERE id=:id", userID=session["user_id"])
        cashAmount = userCash[0]["cash"]

        # Subtract cashValue by value of transaction
        cashValue = cashAmount - transactionInfo

        if cashValue < 0:
            return apology("you do not have enough cash", 403)

        # Update how much left in his account (cash) after the transaction
        db.execute("UPDATE users SET cash=:updt_cash WHERE id=:id", cashValue=cashValue, userID=session["user_id"])
        # Update de transactions table
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
                   user_id=session["user_id"], symbol=stock['symbol'], shares=shares, price=stock['price'])
        flash("Bought!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactionInfo = db.execute(
        "SELECT symbol, shares, price, transacted FROM transactions WHERE user_id=:user_id", userID=session["user_id"])
    for index in range(len(transactionInfo)):
        transactionInfo[index]["price"] = usd(transactionInfo[i]["price"])
    return render_template("history.html", transactionInfo=transactionInfo)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Check if the user's username has been sumbitted via register
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Query database for the user's username
        rowInfo = db.execute("SELECT * FROM users WHERE username = :username",
                             userName=request.form.get("username"))

        # Make sure that the username exists and password is correct
        if len(rowInfo) != 1 or not check_password_hash(rowInfo[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Keep track whar user is registered
        session["user_id"] = rowInfo[0]["id"]

        # Redirect user to the home page
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
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure name of stock was submitted
        if not request.form.get("symbol"):
            return apology("must provide stock symbol")

        # Use the lookup function
        dollarSymbol = request.form.get("symbol").upper()
        stockValue = lookup(dollarSymbol)

        # Check if stock is valid
        if stockValue == None:
            return apology("Stock symbol not valid", 400)

        # If its valid
        else:
            return render_template("quoted.html", stockCheck={'name': stockValue['symbol'], 'price': usd(stockValue['price'])})

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    # The user has reached  the route called POST
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password was submitted
        elif not request.form.get("password_confirm"):
            return apology("must provide password confirmation", 400)

        # Ensure confirmation password is equal to password
        elif request.form.get("password") != request.form.get("password_confirm"):
            return apology("password dont match", 400)
        try:
            # Add into db
            newUser = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", userName=request.form.get(
                "username"), passWordhash=generate_password_hash(request.form.get("password")))

        except:
            # Check if its unique
            return apology("username is already registered", 400)

        # Remember the user
        session["user_id"] = newUser

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # User reached route called POST
    if request.method == "POST":

        # Make sure the stock is sumbitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)

        # Make sure the shares are sumbitted s
        elif not request.form.get("shares"):
            return apology("must provide shares", 403)

        # If shares are greater than 0
        elif int(request.form.get("shares")) < 0:
            return apology("must provide a valid number of shares", 403)

        # Make sure the symbol is valid
        if not request.form.get("symbol"):
            return apology("must provide an existing symbol", 403)

        # Uppercase the symbol
        dollarSymbol = request.form.get("symbol").upper()
        stockValue = lookup(dollarSymbol)

        rowInfo = db.execute(
            "SELECT symbol, SUM(shares) FROM transactions WHERE user_id=:user_id GROUP BY symbol HAVING SUM(shares) > 0", userID=session["user_id"])

        # The transaction values
        numShares = int(request.form.get("shares"))
        for index in rowInfo:
            if index["symbol"] == symbol:
                if numShares > index["SUM(shares)"]:
                    return apology("you're doing something wrong", 403)

        transactionInfo = numShares * stockValue['price']

        # Determine if the user has enough cash
        userCash = db.execute("SELECT cash FROM users WHERE id=:id", userID=session["user_id"])
        cashAmount = userCash[0]["cash"]

        # Get the difference of the user's cash from their transaction
        cashValue = cashAmount + transactionInfo

        # Update the information of the user's transactions
        db.execute("UPDATE users SET cash=:updt_cash WHERE id=:id", cashValue=cashValue, userID=session["user_id"])
        # Make sure the transaction's table is update
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
                   userID=session["user_id"], dollarSymbol=stockValue['symbol'], numShares=-1 * numShares, stockPrice=stockValue['price'])
        flash("Sold!")
        return redirect("/")

    # User has reached the route called GET
    else:
        rowInfo = db.execute(
            "SELECT symbol FROM transactions WHERE user_id=:user_id GROUP BY symbol HAVING SUM(shares) > 0", userID=session["user_id"])
        return render_template("sell.html", symbolNotation=[index["symbol"] for index in rowInfo])

# The handler for errors


def errorhandler(error):
    """Handle error"""
    if not isinstance(error, HTTPException):
        error = InternalServerError()
    return apology(error.name, error.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)