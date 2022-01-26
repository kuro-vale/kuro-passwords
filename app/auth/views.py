# App
from app.auth.models import UserModel, UserData
from app.firestore_service import get_user, post_user
from app.forms import LoginForm
# Flask
from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import current_user, login_user, login_required, logout_user
# Werkzeug
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_doc = get_user(username)
        if user_doc.to_dict() is not None:
            if check_password_hash(user_doc.to_dict()["password"], password):
                user_data = UserData(username, password)
                user = UserModel(user_data)
                login_user(user)
                return redirect(url_for("index"))
            else:
                flash("Invalid information")
        else:
            flash("User Doesn't exist")
    return render_template("login.html", form=form)


@auth.route("signup", methods=["GET", "POST"])
def signup():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_doc = get_user(username)
        if user_doc.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash)
            post_user(user_data)
            user = UserModel(user_data)
            login_user(user)
            flash("Successfully register")
            return redirect(url_for("index"))
        else:
            flash("Username already exists")
    return render_template("signup.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Successfully logout")
    return redirect(url_for("auth.login"))
