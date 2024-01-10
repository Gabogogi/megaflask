from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
# a database instance and dtabse engine will be created here
db = SQLAlchemy(app)
# migrate is the database migration engine
migrate = Migrate(app, db)

# module defines the structure of the database
from app import routes, models