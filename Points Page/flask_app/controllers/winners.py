from flask import Flask, render_template, request, redirect, url_for, session
from flask_app import app
from flask_app.models.winners import Winners

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/main")
def index():
    return render_template("index.html", users=Winners.get_all())

# @app.route("/")
# def index():
#     if "user_id" in session:
#         return render_template("index.html", users=Winners.get_all())
#     else:
#         return redirect("/login")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "southside" and password == "hotsauce":
            session["logged_in"] = True
            return redirect("/main")
        else:
            error_message = "Invalid username or password"
            return render_template("login.html", error_message=error_message)

    return render_template("login.html", error_message=None)

@app.route("/add/<int:user_id>", methods=["POST"])
def add(user_id):
    Winners.add_points(user_id, points=1) # Add 1 point
    return redirect("/")

@app.route("/subtract/<int:user_id>", methods=["POST"])
def subtract(user_id):
    Winners.subtract_points(user_id, points=1)  # Subtract 1 point
    return redirect("/")

@app.route("/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    data = {'user_id': user_id}
    Winners.delete_user(data)
    return redirect("/")

@app.route("/add_user", methods=["POST"])
def add_user():
    data = {
        'name': request.form['name'],
        'points': request.form['points']
    }
    Winners.save(data)
    return redirect("/")
