#!/usr/bin/python3

""" Index file """

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def count_objects():
    """ count the number of objects in each class"""
    object_names = {
            'states': 'State',
            'cities': 'City',
            'amenities': 'Amenity',
            'places': 'Place',
            'reviews': 'Review',
            'users': 'User'
    }

    objects = {name: storage.count(classes[cls_name]) for name,
               cls_name in object_names.items()}
    return jsonify(objects)
