# server/seed.py
from server.app import create_app, db
from server.models import Guest, Episode, Appearance, User
from datetime import date

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create Users
    user = User(username="admin")
    user.set_password("password")
    db.session.add(user)

    # Create Guests
    guest1 = Guest(name="Tom Hanks", occupation="Actor")
    guest2 = Guest(name="Adele", occupation="Singer")
    db.session.add_all([guest1, guest2])

    # Create Episodes
    episode1 = Episode(date=date(2024, 6, 1), number=1)
    episode2 = Episode(date=date(2024, 6, 2), number=2)
    db.session.add_all([episode1, episode2])

    # Create Appearances
    appearance1 = Appearance(rating=5, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=4, guest=guest2, episode=episode1)
    appearance3 = Appearance(rating=3, guest=guest1, episode=episode2)
    db.session.add_all([appearance1, appearance2, appearance3])

    db.session.commit()
    print("Database seeded successfully.")
