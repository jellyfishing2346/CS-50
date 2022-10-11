
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/index")
def index():
    # Build Sql Connection, get all rows and return the json object of it
    with sqlite3.connect("company.db") as row:
        cursor = row.cursor()
        cursor.execute("SELECT * FROM employees")
        db_students = cursor.fetchall()
    return jsonify(db_students)

@app.route("/add", methods=["POST"])
def add():
    # Build Sql Connection, insert the values that come from the querystring
    with sqlite3.connect("company.db") as row:
        cursor = row.cursor()
        cursor.execute("INSERT INTO employees (firstname, lastname, birthdate, age, sex, class_per_week, class_group) VALUES (?,?,?,?,?,?,?)",
            (request.args.get("firstName", ""),
            request.args.get("lastName", ""),
            request.args.get("birthdate", ""),
            request.args.get("age", ""),
            request.args.get("gender", ""),
            int(request.args.get("class", "")),
            request.args.get("school year", "")))
    return "200"

@app.route("/delete", methods=["POST"])
def delete():
    # Build Sql Connection, get UID from querystring and execute Delete Statements
    if request.args.get("uid", ""):
        with sqlite3.connect("school.db") as row:
            cursor = row.cursor()
            cursor.execute("DELETE FROM employees WHERE id = (?)", (request.args.get("uid",""),))
        return "200"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)

