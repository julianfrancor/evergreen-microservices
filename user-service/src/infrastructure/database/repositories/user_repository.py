# src/infrastructure/database/repositories/user_repository.py
from infrastructure.database.database import Session
from infrastructure.database.models.user_model import UserModel
from domain.user import User

class UserRepository:
    def create_user(self, user):
        session = Session()
        user_model = UserModel(username=user.username, email=user.email, full_name=user.full_name)
        session.add(user_model)
        session.commit()
        session.close()
        return user_model

    def get_user(self, user_id):
        session = Session()
        user = session.query(UserModel).filter_by(id=user_id).first()
        session.close()
        return user

    def get_all_users(self):
        session = Session()
        users = session.query(UserModel).all()
        session.close()
        return users

    def update_user(self, user_id, user):
        session = Session()
        user_model = session.query(UserModel).filter_by(id=user_id).first()
        user_model.username = user.username
        user_model.email = user.email
        user_model.full_name = user.full_name
        session.commit()
        session.close()
        return user_model

    def delete_user(self, user_id):
        session = Session()
        user = session.query(UserModel).filter_by(id=user_id).first()
        session.delete(user)
        session.commit()
        session.close()
