from flask import request
from flask_restplus import Resource
from .. import db, flask_bcrypt
from ..model.dto import ItemDto
from app.main.model.model import ItemType

api = ItemDto.api
_item_type = ItemDto.item_type

@api.route('/type', defaults={'type_id': None})
@api.route('/type/<type_id>')
@api.param('type_id')
class ItemTypeController(Resource):
    @api.doc('item_type_by_id')
    @api.marshal_with(_item_type)
    def get(self, type_id):
        t = db.session.query(ItemType).filter_by(id=type_id).first()
        return t

    @api.doc('update_item_type')
    @api.response(201, 'updated item type')
    @api.expect(_item_type)
    def post(self, type_id):
        data = request.json
        item_type = ItemType.query.filter_by(id=data['id']).first()

        if not item_type:
            item_type = ItemType()

        item_type.name = data['name']
        item_type.description = data['description']
        item_type.predecessor = ItemType.query.filter_by(id=data['predecessor_id']).first()

        db.session.add(item_type)
        db.session.commit()

        return