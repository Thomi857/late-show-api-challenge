# server/controllers/episode_controller.py
from flask import Blueprint, jsonify, request
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.app import db
from flask_jwt_extended import jwt_required

bp = Blueprint("episodes", __name__)

@bp.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    data = [{"id": e.id, "date": e.date.isoformat(), "number": e.number} for e in episodes]
    return jsonify(data), 200

@bp.route("/episodes/<int:id>", methods=["GET"])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = [
        {
            "id": a.id,
            "rating": a.rating,
            "guest_id": a.guest_id,
            "episode_id": a.episode_id
        }
        for a in episode.appearances
    ]
    data = {
        "id": episode.id,
        "date": episode.date.isoformat(),
        "number": episode.number,
        "appearances": appearances
    }
    return jsonify(data), 200

@bp.route("/episodes/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"message": "Episode deleted"}), 200
