# server/controllers/guest_controller.py
from flask import Blueprint, jsonify
from server.models.guest import Guest

bp = Blueprint("guests", __name__)

@bp.route("/guests", methods=["GET"])
def get_guests():
    guests = Guest.query.all()
    guest_list = [{"id": g.id, "name": g.name, "occupation": g.occupation} for g in guests]
    return jsonify(guest_list), 200