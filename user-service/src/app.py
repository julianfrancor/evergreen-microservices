# app.py
from flask import Flask
from interfaces.controllers.user_controller import user_controller

app = Flask(__name__)

app.register_blueprint(user_controller)

if __name__ == '__main__':
    app.run(debug=True)
