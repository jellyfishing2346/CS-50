import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.methods == "POST":
        # Enter the user's entry to the database
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        #Insert data into database
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?,?, ?)", name, month, day)
        return redirect("/")
    else:
        # Display the database entries on index.html
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=birthdays)
