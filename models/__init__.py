from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User  # Import your models here