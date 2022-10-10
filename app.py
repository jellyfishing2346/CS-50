david232323
#6364

david232323
 —
Today at 3:09 PM
The issue is now that stockName is not defined

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():

    if request.method == "POST":
        quotes = lookup(request.form.get("symbol"))

Expand
SPOILER_message.txt1 KB
https://submit.cs50.io/check50/eab0cc0126d738f4b4598f78a810235e172b0750
What do you think
@al1matte0
al1matte0
 —
Today at 3:49 PM
sorry i was afk
show me the error message? are you getting past the previous invald ticker one?
because yeah, stockname has no assigned variable
you'll  need to do something like stockname = lockup(request.form.get("stock"))
or something
in your sql database, you'll want at least 2 tables, one is the premade users, the other is for the transactions user does ##sidenote i'm still on this pset, and adding features, so maybe 3 tables could be used but for now i'm just doing two##
so in your second table (that you made) you'll have all the user info, what they own, cash, etc
in there you'd want to take the name of a specific stock i think
david232323
 —
Today at 3:53 PM
Let me try that
al1matte0
 —
Today at 3:53 PM
i feel i may just be making this worse tbh lmao
like in my quote html, i have the name of the value as stock
<input autocomplete="off" autofocus class="form-control mx-auto w-auto" id="symbol" name="symbol" placeholder="Symbol" type="text">
sorry symbol
if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Please input a symbol")

        stock = lookup(symbol)

        if not stock:
            return apology("Symbol isn't valid")
        return render_template("quoted.html", stock = stock)
    else:
        return render_template("quote.html")
then only that for my python code for quote
david232323
 —
Today at 3:59 PM
Image
I get some attribute error

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask.helpers import get_flashed_messages
from flask_session import Session
from helpers import apology, login_required, lookup, usd
from tempfile import mkdtemp

Expand
SPOILER_message.txt10 KB
You there?
@al1matte0
al1matte0
 —
Today at 4:11 PM
what's your html look like lol
move the .upper() from the html to the main i'm thinking?
david232323
 —
Today at 4:12 PM

<!DOCTYPE html>
<form {% extends "layout.html" %}

{% block title %}
    Quoted
{% endblock %}></form>

Expand
SPOILER_message.txt1 KB
I don't see the upper()
al1matte0
 —
Today at 4:13 PM
it's not in your main
and i don't see it in your quoted html either
okay that's odd
david232323
 —
Today at 4:14 PM
Yeah
al1matte0
 —
Today at 4:15 PM
quotes = request.form.get("symbol").upper()
try that
my bad, it want's the upper function bc the symbol names are all capitalized
david232323
 —
Today at 4:17 PM
https://submit.cs50.io/check50/0bb871d8e2de8019da0863186aabf8e8418289e4
No it didn't work
Hold on
No it didn't work
Why is there upper()
david232323
 —
Today at 4:23 PM
Which is it
@al1matte0
al1matte0
 —
Today at 4:31 PM
https://www.reddit.com/r/cs50/comments/7rirnw/problem_set7_check50_errors/
reddit
r/cs50 - Problem Set7 Check50 Errors
7 votes and 11 comments so far on Reddit
I didn't format the price of stock by usd(). When I changed my code from {{ price }} to {{ price | usd }} in quoted.html, it worked.
sorry i'm kinda afk and shit at the moment
david232323
 —
Today at 4:36 PM
I removed the places where I used the usd() and only used | usd. Tho it still gives me the attribute error for not having upper
I mean I have everything like you did, but nothing works
This shitty check50 is just being a massive redudnant
al1matte0
 —
Today at 4:49 PM
IT IS
oop sorry caps
i best bet, resave the whole project and go thru and remake everything
that's what i did (twice actually) lmao
alexandria's video was pretty spot on if you follow the idea
david232323
 —
Today at 4:50 PM
I saw her video it much help
al1matte0
 —
Today at 4:50 PM
https://github.com/code50/109174696/blob/e72f55f7325ac8eda4dc46859fe02d3d9fc5e169/KEEPTHIS/WORKINGFINANCE
that's my finished code before i added like add cash and change password (and some minor aesthetic crap)
that should run fully and fine, and although you shouldn't cheat, it's there lol
david232323
 —
Today at 4:52 PM
It says page isn't found
al1matte0
 —
Today at 4:52 PM
urghhh
david232323
 —
Today at 4:52 PM
😦
al1matte0
 —
Today at 4:53 PM
https://github.com/code50/109174696/archive/d9e4c6839ff7bdc102d5d90f55935ff32c005c4c.zip
can you download from there?
david232323
 —
Today at 4:54 PM
I still get page not found
al1matte0
 —
Today at 4:54 PM
goddamn
david232323
 —
Today at 4:55 PM
Yeah idk why that is happening
al1matte0
 —
Today at 4:55 PM

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

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"] # Sets current session

    stocks = db.execute("SELECT symbol, name, price, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

    total = cash

    for stock in stocks:
        total += stock["price"] * stock["total_shares"]
    return render_template("index.html", stocks = stocks, cash = cash, usd = usd, total = total)
    #can also do usd(cash) as above



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        stock = lookup(symbol)
        if not symbol:
            return apology("Please input a symbol")
        elif not stock:
            return apology("Symbol isn't valid")

        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Share must be an integer")

        if shares <= 0:
            return apology("Share value must be a positive integer please")


        user_id = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        stock_name = stock["name"]
        stock_price = stock["price"]
        total_price = stock_price * shares

        if cash < total_price:
            return apology("Insufficient Funds")
        else:
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - total_price, user_id)
            db.execute("INSERT INTO transactions (user_id, name, shares, price, type, symbol) VALUES (?, ?, ?, ?, ?, ?)", user_id, stock_name, shares, stock_price, 'buy', symbol)
            #in the above (and in the sql in general) the 'type' row seems kinda pointless

        flash("Purchased.")
        return redirect('/')


    else:
... (136 lines left)

Collapse
app.py8 KB
david232323
 —
Today at 4:55 PM
I see it now
al1matte0
 —
Today at 4:55 PM
aye
lmao
well that's my application file
david232323
 —
Today at 4:56 PM
yeah
al1matte0
 —
Today at 4:56 PM
wont let me upload the html ones for some reason
they're all pretty small though
david232323
 —
Today at 4:56 PM
thats odd
al1matte0
 —
Today at 4:56 PM
anyway, that should work for a guide
david232323
 —
Today at 4:56 PM
ok sounds good
al1matte0
 —
Today at 4:56 PM
(i think discord is trying to run them bc html)
david232323
 —
Today at 4:56 PM
probably
﻿

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

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"] # Sets current session

    stocks = db.execute("SELECT symbol, name, price, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

    total = cash

    for stock in stocks:
        total += stock["price"] * stock["total_shares"]
    return render_template("index.html", stocks = stocks, cash = cash, usd = usd, total = total)
    #can also do usd(cash) as above



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        stock = lookup(symbol)
        if not symbol:
            return apology("Please input a symbol")
        elif not stock:
            return apology("Symbol isn't valid")

        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Share must be an integer")

        if shares <= 0:
            return apology("Share value must be a positive integer please")


        user_id = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        stock_name = stock["name"]
        stock_price = stock["price"]
        total_price = stock_price * shares

        if cash < total_price:
            return apology("Insufficient Funds")
        else:
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - total_price, user_id)
            db.execute("INSERT INTO transactions (user_id, name, shares, price, type, symbol) VALUES (?, ?, ?, ?, ?, ?)", user_id, stock_name, shares, stock_price, 'buy', symbol)
            #in the above (and in the sql in general) the 'type' row seems kinda pointless

        flash("Purchased.")
        return redirect('/')


    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions = db.execute("SELECT type, symbol, price, shares, time FROM transactions WHERE user_id = ?", user_id)
    return render_template("history.html", transactions = transactions, usd = usd)


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
    if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Please input a symbol")

        stock = lookup(symbol)

        if not stock:
            return apology("Symbol isn't valid")
        return render_template("quoted.html", stock = stock)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Please enter a username")
        elif not password:
            return apology("Please enter a password")
        elif not confirmation:
            return apology("Please confirm your password")
        if password != confirmation:
            return apology("Passwords do not match")

        try:
            hash = generate_password_hash(password)
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            return redirect('/')
        except:
            return apology("Username is already taken")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        user_id = session["user_id"]
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        if shares <= 0:
            return apology("Share not valid. Please enter a positive integer.")

        stock_price = lookup(symbol)["price"]
        stock_name = lookup(symbol)["name"]
        price = shares * stock_price

        shares_owned = db.execute("SELECT SUM(shares) FROM transactions WHERE user_id = ? AND symbol = ?", user_id, symbol)[0]["SUM(shares)"]
        if shares_owned < shares:
            return apology("Not enough shares")

        current_balance = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        db.execute("UPDATE users SET cash = ? WHERE id = ?", current_balance + price, user_id)
        db.execute("INSERT INTO transactions (user_id, name, shares, price, type, symbol) VALUES (?, ?, ?, ?, ?, ?)", user_id, stock_name, -shares, stock_price, "sell", symbol)
        flash("Sold.")
        return redirect('/')

    else:
        user_id = session["user_id"]
        symbols = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
        return render_template("sell.html", symbols = symbols)
