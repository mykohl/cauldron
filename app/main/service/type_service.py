import flask
import sys
import config
from app.main.model.model import ItemType
from .. import db, flask_bcrypt

def get_item_type_path(item_type_id):
    i = db.session.query(ItemType).filter_by(id = item_type_id).first()
    path = i.name

    if i.predecessor_id is not None:
        path = get_item_type(i.predecessor_id) + ' : ' + path

    return path

