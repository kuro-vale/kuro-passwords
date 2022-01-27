# App
from app import create_app
from app.firestore_service import post_log, get_logs, get_passwords, post_password, delete_password, update_password
from app.forms import PasswordForm
# Python
import random
import string
from datetime import datetime
# Flask
from flask import request, redirect, render_template, flash, url_for
from flask_login import login_required, current_user

app = create_app()


# Home paths
@app.route("/")
def index():
    user_ip = request.remote_addr
    # Save login log
    if current_user.is_authenticated:
        date = datetime.now()
        user_id = current_user.id
        post_log(user_ip, date, user_id)
    return redirect("/home")


@app.route("/home", methods=["GET", "POST"])
@login_required
def home():
    user_id = current_user.id
    passwords = get_passwords(user_id)
    password_form = PasswordForm()
    context = {
        "username": user_id,
        "passwords": passwords,
        "form": password_form
    }
    # Save new password
    if password_form.validate_on_submit():
        site = password_form.site.data
        username = password_form.username.data
        password = password_form.password.data
        post_password(site, username, password, user_id)
        flash("Password added")
        return redirect(url_for("home"))
    return render_template("home.html", **context)


# Methods Paths
@app.route("/random")
def generate_random_password():
    characters = list(string.ascii_letters + string.digits + string.punctuation)
    random.shuffle(characters)
    random_password = []
    for i in range(15):
        random_password.append(random.choice(characters))
    random.shuffle(random_password)
    flash("".join(random_password))
    return redirect(request.referrer)


@app.route("/logs")
@login_required
def show_logs():
    user_id = current_user.id
    logs = get_logs(user_id)
    return render_template("logs.html", logs=logs)


@app.route("/<password_id>/delete")
def delete(password_id):
    user_id = current_user.id
    delete_password(password_id, user_id)
    flash("Password Deleted")
    return redirect(url_for("home"))


@app.route("/<password_id>/update", methods=["GET", "POST"])
def update(password_id):
    user_id = current_user.id
    password_form = PasswordForm()
    if password_form.validate_on_submit():
        site = password_form.site.data
        username = password_form.username.data
        password = password_form.password.data
        update_password(password_id, site, username, password, user_id)
        flash("Password Updated")
        return redirect(url_for("home"))
    return render_template("update.html", form=password_form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
