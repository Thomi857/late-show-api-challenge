from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

    # ✅ Use string for relationship target to avoid early resolution errors
    appearances = db.relationship("Appearance", backref="guest", cascade="all, delete-orphan")
