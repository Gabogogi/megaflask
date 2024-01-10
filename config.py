import os
basedir = os.path.abspath(os.path.dirname(__file__))
# basedir sets the location of the database

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'abretusalas'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
# configuration and environment variables should be kept apart
# provide a fallback value ie app.db, a database called app.db