import os


class Config:
    # Define the application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Statement for enabling the development environment
    DEBUG = True

    # Define the database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection against *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"


class TestConfig(Config):
    # Define the database settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
