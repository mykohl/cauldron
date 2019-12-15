from sqlalchemy.ext.declarative import declared_attr
from .. import db, flask_bcrypt

class TableMixin(object):
    @declared_attr
    def __tablename__(self):
        return self.__name__

    id = db.Column(db.Integer, primary_key = True)

    __mapper_args__ = {'always_refresh': True}


class ArticleMixin(object):
    def __init__(self, data = None):
        if data is not None:
            if 'name' in data:
                self.name = data['name']
            if 'description' in data:
                self.description = data['description']

    name = db.Column(db.String)
    description = db.Column(db.String)


class HierarchyMixin(TableMixin, object):
    def __init__(self, data = None):
        if data is not None:
            if 'successors' in data:
                self.successors = list(map(self.__class__, data['successors']))

    @declared_attr
    def predecessor_id(self):
        return db.Column(db.Integer, db.ForeignKey(self.__name__ + '.id'))

    @declared_attr
    def predecessor(self):
        return db.relationship(self.__name__, remote_side = self.__name__ + '.id', backref = 'sucessors')

    @declared_attr
    def successors(self):
        return db.relationship(self.__name__)


class TypeMixin(ArticleMixin, HierarchyMixin, object):
    def __init__(self, data = None):
        if data is not None:
            ArticleMixin.__init__(self, data)
            HierarchyMixin.__init__(self, data)


class DetailMixin(ArticleMixin, object):
    value = db.Column(db.String)
    value_type = db.Column(db.String)


class ComponentMixin(object):
    @declared_attr
    def universe_id(self):
        return db.Column(db.Integer, db.ForeignKey('Universe.id'))


class CreationMixin(object):
    @declared_attr
    def creator_id(self):
        return db.Column(db.Integer, db.ForeignKey('Creator.id'))

    created_on = db.Column(db.Date)
    edited_on = db.Column(db.Date)
