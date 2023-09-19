
from infrastructure.database.repositories.user_repository import UserRepository
from domain.user import User

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, username, email, full_name):
        print("==========" + "HOLA1" + "==========")
        existing_user = self.user_repository.get_user_by_email(email)
        if existing_user:
            return None
        user = User(username=username, email=email, full_name=full_name)
        self.user_repository.create_user(user)
        return user

    def get_user(self, user_id):
        return self.user_repository.get_user(user_id)

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def update_user(self, user_id, username, email, full_name):
        user = User(username, email, full_name)
        return self.user_repository.update_user(user_id, user)

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)

