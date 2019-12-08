from flask_restplus import Namespace, fields

class ItemTypeDto:
    api = Namespace('item_type', description = 'item type operations')
    item_type = api.model('item_type', {
        'name': fields.String(description = 'short name of item type'),
        'path': fields.String(description = 'full hierarchical path to item type node'),
        'root_id': fields.Integer(description = 'item type id for top-level parent')
    })