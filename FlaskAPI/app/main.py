"""The Flask App."""

from flask import Flask, json, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from datetime import date

from . import models
from .database import DATABASE_URL

API_VERSION = "v1"
app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.errorhandler(404)
def resource_not_found(exception):
    """Returns exceptions as part of a json."""
    return jsonify(error=str(exception)), 404


@app.route("/{}/add-item".format(API_VERSION), methods=["POST"])
def add_item():
    """Receives Item and Adds it to Database"""
    try:
        data = request.json
        name = data.get('name', None)
        if name:
            list_item = models.ListItem(name=str(name),date_added=date.today())
            db.session.add(list_item)
            db.session.commit()

            return jsonify(
                message="Item has been Added",
                name=name,
                status =  str(201)
            ),
        else:
            return jsonify(
                message="Failed to Add Item",
                name=name,
                status = str(200)
            )
    except Exception as e:
        return json(
        message = "Exception:{}".format(str(e)),
        items = [],
        count = 0,
        status = str(500)

    )


@app.route("/{}/all-items".format(API_VERSION), methods=["GET"])
def all_items():
    """Return All Items"""
    try:
            list_items =  db.session.query(models.ListItem).all()
            return jsonify(
            message= "Items Found!",
            items=[i.serialize for i in list_items],
            count = len(list_items),
            status = str(200)
        )
    except Exception as e:
        return json(
            message = "Exception:{}".format(str(e)),
            items = [],
            count = 0,
            status = str(200)
        )

@app.route("/{}/search-item".format(API_VERSION), methods=["POST"])
def search_items():
    """Search for Item"""
    try:
        search_primer = request.json.get("search_primer", None)
        if not search_primer: return jsonify(message="No Items Found!",
        items=[]
        )

        list_items =  db.session.query(models.ListItem).all()
        if list_items:
            # filter items based on search key
            list_items = [
                i.serialize for i in list_items if search_primer in str(
                    i.serialize.get("name", ""))
            ]
            
        return jsonify(
        message = "Items Found!" if len(list_items)>0 else "No Items Found",
        items=[i for i in list_items
        ],
        count = len(list_items),
        status = str(200),
        )
    except Exception as e:
        return jsonify(
            message = "Exception:{}".format(str(e)),
            count = 0,
            items =[],
            status = str(500)
        )

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
