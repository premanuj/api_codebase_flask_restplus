""" Meta information about the database connection """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = db.Model
session = db.session
