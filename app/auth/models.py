# App
from app.firestore_service import get_user
# Flask
from flask_login import UserMixin


class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserModel(UserMixin):
    def __init__(self, user_data):
        """
        :param user_data: UserData
        """
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(user_id):
        user_doc = get_user(user_id)
        user_data = UserData(user_doc.id, user_doc.to_dict()["password"])
        return UserModel(user_data)
