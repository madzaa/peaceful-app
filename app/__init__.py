"""Main application package."""
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.logger.setLevel(logging.INFO)

from app import models
from app import views