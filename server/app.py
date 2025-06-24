# server/app.py
from flask import Flask
from server.config import Config, db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)


    # Import models to register with SQLAlchemy
    from server.models import user, guest, episode, appearance

    # Import and register blueprints
    from server.controllers.auth_controller import bp as auth_bp
    from server.controllers.guest_controller import bp as guest_bp
    from server.controllers.episode_controller import bp as episode_bp
    from server.controllers.appearance_controller import bp as appearance_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(appearance_bp)

    return app

# For running the app directly
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)