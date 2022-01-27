# Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential, {"projectId": "flask-passwords"})
db = firestore.client()


def get_user(user_id):
    return db.document(f"users/{user_id}").get()


def get_logs(user_id):
    return db.collection(f"users/{user_id}/logs").get()


def get_passwords(user_id):
    return db.collection(f"users/{user_id}/passwords").get()


def post_user(user_data):
    user_ref = db.document(f"users/{user_data.username}")
    user_ref.set({"password": user_data.password})


def post_log(ip, date, user_id):
    logs_ref = db.collection(f"users/{user_id}/logs")
    logs_ref.add({"IP": ip, "Date": date})


def post_password(site, username, password, user_id):
    passwords_ref = db.collection(f"users/{user_id}/passwords")
    passwords_ref.add({"Site": site, "Username": username, "Password": password})


def delete_password(password_id, user_id):
    password_ref = db.document(f"users/{user_id}/passwords/{password_id}")
    password_ref.delete()


def update_password(password_id, site, username, password, user_id):
    password_ref = db.document(f"users/{user_id}/passwords/{password_id}")
    password_ref.update({"Site": site, "Username": username, "Password": password})
