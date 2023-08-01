#!/usr/bin/python3

"""index file"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """return status"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """return stats"""
    classes = ["Amenity", "City", "Place", "Review", "State", "User"]
    counts = {}
    for cls in classes:
        counts[cls.lower()] = storage.count(cls)
    return jsonify(counts)
