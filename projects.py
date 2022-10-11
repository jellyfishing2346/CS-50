from flask import Flask, flash, redirect, render_template, request, session
import datetime
import urllib3
from urllib.parse import urlencode
import json

# Create a flask app instance
app = Flask(__name__)

http = urllib3.PoolManager()

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    # get the list of all employees from the backend
    list = http.request('GET','localhost:5001/index')
    db_students = json.loads(list.data.decode('utf-8'))
    return render_template("index.html", db_students=db_students)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Convert all attributes in an object and give this object to the end
        birthday = datetime.date(int(request.form["year"]),int(request.form["month"]),int(request.form["day"])).isoformat()
        args = {
            "firstName":request.form.get("firstName"),
            "lastName":request.form.get("lastName"),
            "birthdate": birthday,
            "age":datetime.datetime.now().year - int(request.form.get("year")),
            "gender":request.form.get("gender"),
            "workload":request.form.get("workload"),
            "class":request.form.get("class")
        }
        # Encode all argument to a query string usage
        url_args = urlencode(args)
        list = http.request("POST","localhost:5001/add?" + url_args)
        return redirect("/")
    return render_template("add.html")

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        # Build an object with the UID that should be deleted
        args = {
            "uid": request.form["uid"]
        }
        # Encode object to a querystring
        url_args = urlencode(args)
        list = http.request("POST","localhost:5001/delete?" + url_args)
    return redirect("/")