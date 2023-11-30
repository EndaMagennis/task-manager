import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env

# Create an instance of Flask and store it in a variable called app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Create an instance of SQLAlchemy and store it in a variable called db
db = SQLAlchemy(app)

# Import the routes module from the taskmanager package
from taskmanager import routes