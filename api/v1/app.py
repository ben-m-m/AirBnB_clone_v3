#!/usr/bin/python3

"""Imports a model"""

from flask import Flask
from os import getenv
from models import storage
from api.v1.views import app_views


app = Flask(__name__)

app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    return {"error": "Not found"}, 404


@app.teardown_appcontext
def teardown_db(exception=None):
    """call"""
    storage.close()


if __name__ == "__main__":
    """main"""
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)

    app.run(host=host, port=port, threaded=True)
