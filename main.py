# App
from app import create_app
# Flask
from flask import request, session, make_response, redirect, render_template
from flask_login import login_required, current_user

app = create_app()


# Home paths
@app.route("/")
def index():
    user_ip = request.remote_addr
    session["user_ip"] = user_ip
    response = make_response(redirect("/home"))
    return response


@app.route("/home")
@login_required
def home():
    username = current_user.id
    context = {
        "username": username
    }
    return render_template("home.html", **context)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
