# Import the os module to interact with the operating system
import os

# Import Flask to create an instance of the Flask web application
from flask import Flask

# Import SQLAlchemy to interact with the database
from flask_sqlalchemy import SQLAlchemy

# Check if the env.py file exists and import it if it does
if os.path.exists("env.py"):
    import env

# Create an instance of Flask and store it in a variable called app
app = Flask(__name__)

# Configure the secret key and the database URI for the Flask application
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Create an instance of SQLAlchemy and store it in a variable called db
db = SQLAlchemy(app)


from taskmanager import routes  # noqa
