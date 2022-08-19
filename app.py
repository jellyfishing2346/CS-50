import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

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

# Checking the API Key
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via GET
    if request.method == "GET":
        return render_template("buy.html")

    # User reached route via POST
    else:

        # Ensures the user inputs symbol and number if shares of a company
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)
        elif not request.form.get("shares"):
            return apology("must provide number of shares", 403)

        # Checks if the symbol is valid
        if not lookup(request.form.get("symbol")):
            return apology("symbol not valid", 403)

        # Queries the data of the user for their balance
        current = db.execute("SELECT cash FROM users WHERE id=:user", user=session["user_id"])

        # Extracts the number of shares the user wants to buy
        quantity = int(request.form.get("shares"))

        # Finds the quote of the holdings based on the symbol the user wants to buy from
        quote = lookup(request.form.get("symbol"))

        # Calculates the cost of the shares according to current price of shares
        cost = quote["price"] * quantity

        # Checks if user has enough money
        if cost > current[0]["cash"]:
            return apology("price of shares exceed cash owned", 403)

        # Error occured here!
        db.execute("INSERT INTO buy (user_id, holdings, quantity, time) VALUES (:user_id, :holdings, :quantity, datetime('now'));",
                  user_id=session["user_id"],
                  holdings=quote["symbol"],
                  quantity=quantity)

        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


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
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

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
    """Get stock quote."""

    # User reached route via POST (submitting symbol)
    if request.method == "POST":

        # Looks up for the information of a company's shares according to symbol
        info = lookup(request.form.get("symbol"))

        # Checks if the symbol is valid
        if info:

            # renders a new template with the corresponding stock quote
            return render_template("quoted.html", info=info)

        else:
            return apology("invalid symbol", 403)


    # User reached route via GET
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (submitting data to be registered)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure confirmation password was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation password", 403)

        # Query database for existing username
        name = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensures if username is not yet taken
        if len(name) == 1:
            return apology("username already exists", 403)

        # Checks if both passwords match
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 403)

        # Inserts new user into database
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :password)",
                   username=request.form.get("username"), password=generate_password_hash(request.form.get("password")))

        return redirect("/")

    # User reached route via GET
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)



