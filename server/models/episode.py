from server.app import db

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    number = db.Column(db.Integer)

    appearances = db.relationship("Appearance", backref="episode", cascade="all, delete-orphan")
