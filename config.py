"""Stores parameters for programs accross this project."""

class AppConfig():
    """Stores parameter variables for flask app."""
    SECRET_KEY = 'my web'
    SESSION_TYPE = 'filesystem'
    #1000 mb max
    MAX_CONTENT_LENGTH = 1024 * 1024 * 1000
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = True
    UPLOAD_FOLDER = '/'

class DatabaseConfig():
    """Config parameters for sql connections are stored here."""
    USER="root"
    DATABASE="flask_project"
    PASSWORD="asdfghjkl;'"
    HOST="localhost"
    MAX_ALLOWED_PACKET = str(AppConfig.MAX_CONTENT_LENGTH)

class SuperUser():
    """Config parameters for Admin account, used in subprocess."""
    PASSWORD = "asdfghjkl;'"
