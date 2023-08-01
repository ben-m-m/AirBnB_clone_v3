#!/usr/bin/python3
"""view for State objects that handles all default RESTFul API actions"""
from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def states_obj():
    """Retrieves the list of all State objects"""
    states_lst = storage.all('State')
    return jsonify([obj.to_dict() for obj in states_lst.values()])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def state_obj():
    """Retrieves a State object"""
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def del_state():
    """Deletes a State object"""
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    state.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a State"""
    nw_state = request.get_json()
    if not nw_state:
        abort(400, "Not a JSON")
    if "name" not in nw_state:
        abort(400, "Missing name")
    state = State(**nw_state)
    storage.new(state)
    storage.save()
    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state():
    """Updates a State object"""
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    body_request = request.get_json()
    if not body_request:
        abort(400, "Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']
    for k, v in body_request.items():
        if k not in ignore:
            setattr(state, key, value)
    storage.save()
    return make_response(jsonify(state.to_dict()), 200)
