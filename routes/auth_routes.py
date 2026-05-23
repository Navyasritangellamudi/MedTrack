from flask import Blueprint, render_template, request, redirect
from services.dynamodb_service import register_user, get_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = {
            "email": request.form["email"],
            "password": request.form["password"],
            "name": request.form["name"]
        }
        register_user(user)
        return redirect("/login")

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = get_user(email)

        if user and user["password"] == password:
            return redirect("/dashboard")

    return render_template("login.html")


@auth_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
