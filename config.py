import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to the database
# Just change the names of your database and crendtials and all to connect to your local system
DB_NAME = "fyyur"
username = 'postgres'
password = 'su'
url = 'localhost'
SQLALCHEMY_DATABASE_URI = "postgres://{}:{}@{}/{}".format(username, password, url, DB_NAME)
