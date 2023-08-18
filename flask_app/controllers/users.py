from flask import render_template,redirect,request, url_for
from flask_app import app
from flask_app.models.users import UserPointsManager

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


user_manager = UserPointsManager()

@app.route("/")
def index():
    users = user_manager.get_users()
    return render_template("index.html", users=users)

@app.route("/add_user", methods=["POST"])
def add_user():
    username = request.form.get("username")
    user_manager.add_user(username)
    return redirect(url_for("index"))

@app.route("/subtract_points/<int:user_id>/<int:points>", methods=["POST"])
def subtract_points(user_id, points):
    user_manager.subtract_points(user_id, points)
    return redirect(url_for("index"))

@app.route("/add_points/<int:user_id>/<int:points>", methods=["POST"])
def add_points(user_id, points):
    user_manager.update_points(user_id, points)
    return redirect(url_for("index"))

@app.route("/delete_user/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    user_manager.delete_user(user_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)