from flask import Flask, g
from interfaces.controllers.user_controller import user_controller
import sqlite3

# Create the Flask application
app = Flask(__name__)

# Register the user controller blueprint
app.register_blueprint(user_controller)

# Configure the database connection
app.config['DATABASE'] = 'evergreen.db'

# Function to establish a connection to the database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        # Create a database connection
        db = g._database = connect_to_database()
    return db

# Teardown function to close the database connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def my_view():
    db = get_db()

if __name__ == '__main__':
    app.run(debug=True)
