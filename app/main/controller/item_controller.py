from flask import request
from flask_restplus import Resource

from ..model.dto import ItemTypeDto
from ..service.type_service import 

api = ItemTypeDto.api
_item_type = ItemTypeDto.item_type


@api.route('/item/type/<item_type_id>')
@api.param('item_type_id')
class ItemTypeHierarchy(Resource):
    @api.marshal_with(_item_type)
    def get(self, item_type_id):
        
