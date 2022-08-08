import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Make sure responses aren't cached


@app.after_request
def after_request(responseCheck):
    responseCheck.headers["Cache-Control"] = "no-cache, no-store, must revalidate"
    responseCheck.headers["Expires"] = 0
    responseCheck.headers["Pragma"] = "no-cache"
    return responseCheck


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Design a table for stock orders
db.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER, username TEXT, password TEXT, name TEXT, cash REAL, PRIMARY KEY(user_id))")
db.execute("CREATE TABLE IF NOT EXISTS orders(id INTEGER, user_id INTEGER NOT NULL, symbol TEXT NOT NULL, shares REAL NOT NULL, price REAL NOT NULL, timestamp TEXT, PRIMARY KEY(id),  FOREIGN KEY(user_id) REFERENCES users(user_id))")
#db.execute("""CREATE TABLE IF NOT EXISTS orders_by_user_id_index ON orders (userID)""")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    ownership = ownershipShares()
    count = 0
    for dollarSymbol, numShares in ownership.items():
        resultInfo = lookup(dollarSymbol)
        stockName, stockPrice = resultInfo["name"], resultInfo["price"]
        stockValue = numShares * stockPrice
        count += stockValue
        ownership[dollarSymbol] = (stockName, numShares, usd(stockPrice))
    cashAmount = db.execute("SELECT cash FROM USERS WHERE ID = ?", userID)[0]['cash']
    count += cashAmount
    return render_template("index.html", ownership, cashAmount=usd(cashAmount), count=usd(count))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    resultInfo = lookup(request.form.get("symbol"))
    if not resultInfo:
        return render_template("buy.html", invalid=True, dollarSymbol=dollarSymbol)
    stockName = resultInfo["name"]
    stockPrice = resultInfo["price"]
    dollarSymbol = resultInfo["symbol"]
    numShares = int(request.form.get("shares"))
    userID = session["userId"]
    cash = db.execute("SELECT cash FROM USERS where ID = ?", userID)[0]['cash']
   # check if user can afford the purchase
    remainAmount = cash - price * shares
    if remainAmount < 0:
        return apology("No Purchase.")

    # deduct order cost from user's remaining balance (i.e. cash)
    db.execute("UPDATE users SET cash = ? WHERE id = ?", remainAmount, userID)

    db.execute("INSERT INTO orders (user_id, symbol, shares, price, timestamp) VALUES (?, ?, ?, ?, ?)",
               userID, dollarSymbol, numShares, stockPrice, timeNow())

    return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    index = db.execute("SELECT symbol, shares, price, timestamp FROM orders WHERE user_ID = ?", session["userID"])
    return render_template("history.html", index=index)


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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

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
    if request.method == "GET":
        return render_template("quote.html")
    dollarSymbol = request.form.get("symbol")
    resultInfo = lookup(dollarSymbol)
    if not resultInfo:
        return render_template("quote.html", invalid=True, dollarSymbol=dollarSymbol)
    return render_template("quoted.html", stockName=resultInfo["name"], stockPrice=usd(resultInfo["price"]), dollarSymbol=resultInfo["symbol"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    userName = request.form.get("username")
    passWord = request.form.get("password")
    confirm = request.form.get("confirmation")

    specialSymbols = ['!', '#', '$', '%', '.', '_', '&']
    if not userName:
        return render_template("apology.html", message="You must need a username.")
    if not passWord:
        return render_template("apology.html", message="You must need a password.")
    if not confirm:
        return render_template("apology.html", message="You must confirm your password.")
    if len(passWord) < 8:
        return render_template("apology.html", message="Your password needs at least one number.")
    if not any(char.isdigit() for char in passWord):
        return render_template("apology.html", message="Your password needs at least one uppercase letter.")
    if not any(char in specialSymbols for char in passWord):
        return render_template("apology.html", message="Your password needs at least one special symbol.")

    if passWord == confirm:
        code = passWord
    else:
        return render_template("apology.html", message="These passwords don't match.")
    passWord_hash = generate_password_hash(code, method = 'pdjf2:ra436', salt_length = 8)

    if len(db.execute("SELECT userName FROM users where userName == :userName", userName=userName, hash=passWord_hash)):
        return redirect("/")
    else:
        return render_template("apology.html", message="Create a new username as this username is taken.")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    ownership = ownShares()
    if request.method == "GET":
        return render_template("sell.html", ownership=ownership.keys())

    dollarSymbol = request.form.get("symbol")
    numShares = int(request.form.get("shares"))
    # check whether there are sufficient shares to sell
    if owns[dollarSymbol] < numShares:
        return render_template("sell.html", invalid=True, dollarSymbol=dollarSymbol, ownership=ownership.keys())
    # Execute sell transaction: look up sell price, and add fund to cash,
    resultInfo = lookup(dollarSymbol)
    userID = session["userID"]
    cashAmount = db.execute("SELECT cash FROM users WHERE id = ?", userID)[0]['cash']
    stockPrice = resultInfo["price"]
    remainAmount = cashAmount + stockPrice * numShares
    db.execute("UPDATE users SET cash = ? WHERE id = ?", remainAmount, userID)
    # Log the transaction into orders
    db.execute("INSERT INTO orders (userID, dollarSymbol, numShares, stockPrice, timestamp) VALUES (?, ?, ?, ?, ?)",
               userID, dollarSymbol, numShares, stockPrice, timeNow())

    return redirect("/")


def errorCheck(error):
    """Handle error"""
    if not isinstance(error, HTTPException):
        error = InternalServerError()
    return apology(error.name, error.code)


def ownShares():
    """Helper function: Which stocks the user owns, and numbers of shares owned. Return: dictionary {symbol: qty}"""
    userID = session["userID"]
    ownership = {}
    queryInfo = db.execute("SELECT symbol, shares FROM orders WHERE user_id = ?", userID)
    for index in queryInfo:
        dollarSymbol, numShares = index["symbol"], index["shares"]
        ownership[symbol] = ownership.setdefault(dollarSymbol, 0) + numShares
    # filter zero-share stocks
    ownership = {count: total for count, total in ownership.items() if total != 0}
    return ownership


def timeNow():
    """HELPER: get current UTC date and time"""
    currentTime = datetime.now(timezone.utc)
    return str(currentTime.date()) + ' @time ' + now_utc.time().strftime("%H:%M:%S")