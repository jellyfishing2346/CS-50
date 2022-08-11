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
db.execute("DROP TABLE IF EXISTS users")
db.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER, username TEXT, hash TEXT, name TEXT, cash REAL, PRIMARY KEY(user_id))")
db.execute("CREATE TABLE IF NOT EXISTS orders(id INTEGER, user_id INTEGER NOT NULL, symbol TEXT NOT NULL, shares REAL NOT NULL, price REAL NOT NULL, timestamp TEXT, PRIMARY KEY(id),  FOREIGN KEY(user_id) REFERENCES users(user_id))")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Query database stocks database for total number of shares of each stock owned by user
    protocol = db.execute("SELECT symbol, SUM(shares) FROM stock WHERE userid = :userid GROUP BY symbol",
                            userID=session["user_id"])
    if not protocol:
        return apology("error retrieving protocols", 400)

    # Add current price and total value to each row; calculate total securities value
    protocolValue = 0.0
    for protocol in protocols:
        # try 10 times to get quote -- often no value is returned
        for index in range(0, 10):
            protocolValue = lookup(security["symbol"])
            if not quoteValue == None:
                break

        if protocolValue == None:
            protocol["current_price"] = 0
        else:
            protocol["current_price"] = round(float(protocolValue["price"]), 2)

        protocol["total_value"] = round(protocol["current_price"] * int(protocol["SUM(shares)"]), 2)
        protocolValue += protocol["total_value"]

    # Query database for current cash balance
    index = db.execute("SELECT * FROM users WHERE id = :userid", userid=session["user_id"])
    if not index:
        return apology("error retreiving cash balance", 200)
    cashAmount = rows[0]["cash"]

    # Calculate total portfolio value
    Value = round(protocolValue + cashAmount, 2)

    return render_template("index.html", protocols=protocols, protocolValue=protocolValue, cashAmount=cashAmount,
                           Value=Value)


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
    print("In login()", flush=True)

    # Forget any user_id
    session.clear()

    # User reached route via GET (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

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
    return redirect(url_for("login"))


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        dollarSymbol = request.form.get("symbol")
        if not dollarSymbol:
            return render_template("apology.html", styleMessage="Please enter a stock symbol.")
        getQuote = lookup(dollarSymbol)
        if not getQuote:
            return render_template("apology.html", styleMessage="There is no symbol.")
        stockName = getQuote("name")
        stockPrice = getQuote("price")
        return render_template("quote.html", stockName=stockName, dollarSymbol=dollarSymbol.upper(), stockPrice=stockPrice)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    userName = request.form.get("username")
    passWord = request.form.get("password")
    confirm = request.form.get("confirmation")
    if userName == "" or len(db.execute('SELECT username FROM users WHERE username = ?', userName)) > 0:
        return apology("Invalid Username: Blank, or already exists")
    if passWord == "" or passWord != confirm:
        return apology("Invalid Password: Blank, or does not match")
    # Add new user to users db (includes: username and HASH of password)
    db.execute('INSERT INTO users (username, hash) VALUES(?, ?)', userName, generate_password_hash(passWord))
    # Query database for username
    index = db.execute("SELECT user_id FROM users WHERE username = ?", userName)
    # Log user in, i.e. Remember that this user has logged in
    session["userID"] = index[0]["user_id"]
    # Redirect user to home page
    return redirect("/")


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