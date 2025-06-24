from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:12345@localhost:5432/late_show_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
