# server/controllers/appearance_controller.py
from flask import Blueprint, request, jsonify
from server.models.appearance import Appearance
from server.app import db
from flask_jwt_extended import jwt_required

bp = Blueprint("appearances", __name__)

@bp.route("/appearances", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get("rating")
    guest_id = data.get("guest_id")
    episode_id = data.get("episode_id")

    if not rating or not guest_id or not episode_id:
        return jsonify({"error": "Missing fields"}), 400

    try:
        rating = int(rating)
        if not (1 <= rating <= 5):
            raise ValueError
    except ValueError:
        return jsonify({"error": "Rating must be an integer from 1 to 5"}), 400

    appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(appearance)
    db.session.commit()

    return jsonify({"message": "Appearance created"}), 201
