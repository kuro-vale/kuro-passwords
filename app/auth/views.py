# App
from app.auth.models import UserModel, UserData
from app.firestore_service import get_user
from app.forms import LoginForm
# Flask
from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import current_user, login_user

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
            if user_doc.to_dict()["password"] == password:
                user_data = UserData(username, password)
                user = UserModel(user_data)
                login_user(user)
                return redirect(url_for("home"))
            else:
                flash("Invalid information")
        else:
            flash("User Doesn't exist")
    return render_template("login.html", form=form)
