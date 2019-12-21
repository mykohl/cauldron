from flask_restplus import Namespace, fields
from app.main.model.model import ItemType
from .. import db, flask_bcrypt

class ItemTypePath(fields.Raw):
    def format(self, eid):
        t = db.session.query(ItemType).filter_by(id = eid).first()
        path = t.name

        if t.predecessor_id is not None:
            path = self.format(str(t.predecessor_id)) + ' : ' + path

        return path


class ItemTypeDto:
    api = Namespace('item_type', description = 'item type operations')
    
    item_type = api.model('item_type', {
        'id': fields.Integer,
        'name': fields.String,
        'path': ItemTypePath(attribute = 'predecessor_id'),
        'description': fields.String
    })
    