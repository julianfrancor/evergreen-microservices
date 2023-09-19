# src/domain/user.py
class User:
    def __init__(self, username, email, full_name):
        self.username = username
        self.email = email
        self.full_name = full_name


    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name
            # Add more fields as needed
        }
