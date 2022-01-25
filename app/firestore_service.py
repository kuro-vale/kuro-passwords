# Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential, {"projectId": "flask-passwords"})
db = firestore.client()


def get_user(user_id):
    return db.document(f"users/{user_id}").get()


def post_user(user_data):
    user_ref = db.document(f"users/{user_data.username}")
    user_ref.set({"password": user_data.password})
