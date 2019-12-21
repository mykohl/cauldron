import flask
import sys
import app.main.config
from app.main.model.model import ItemType
from .. import db, flask_bcrypt

def get_one_item_type(item_type_id):
    return db.session.query(ItemType).filter_by(id = item_type_id).first()
