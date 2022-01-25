# App
from app import create_app
from app.firestore_service import post_log, get_logs
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
    if current_user.is_authenticated:
        date = datetime.now()
        username = current_user.id
        post_log(user_ip, date, username)
    return redirect("/home")


@app.route("/home")
@login_required
def home():
    username = current_user.id
    context = {
        "username": username
    }
    return render_template("home.html", **context)


@app.route("/random")
def generate_random_password():
    characters = list(string.ascii_letters + string.digits + string.punctuation)
    random.shuffle(characters)
    random_password = []
    for i in range(15):
        random_password.append(random.choice(characters))
    random.shuffle(random_password)
    flash("".join(random_password))
    return redirect(url_for("home"))


@app.route("/logs")
@login_required
def show_logs():
    username = current_user.id
    logs = get_logs(username)
    return render_template("logs.html", logs=logs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
