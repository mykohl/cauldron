from .. import db, flask_bcrypt
from app.main.model.model_mixins import TableMixin, ArticleMixin, HierarchyMixin, TypeMixin, DetailMixin, ComponentMixin, CreationMixin

class Creator(TableMixin, db.Model):
    name = db.Column(db.String)
    name_first = db.Column(db.String)
    name_last = db.Column(db.String)
    universes = db.relationship('Universe')

    def __repr__(self):
        return "<Creator '{}'>".format(self.name)


class Universe(TableMixin, ArticleMixin, CreationMixin, db.Model):
    items = db.relationship('Item')
    events = db.relationship('Event')


class Item(TableMixin, ArticleMixin, ComponentMixin, CreationMixin, db.Model):
    types = db.relationship('ItemTypeInventory')
    aspects = db.relationship('ItemAspect')


class ItemAspect(TableMixin, ArticleMixin, CreationMixin, db.Model):
    item_id = db.Column(db.Integer, db.ForeignKey('Item.id'))
    details = db.relationship('ItemAspectDetail')


class ItemAspectDetail(TableMixin, DetailMixin, CreationMixin, db.Model):
    item_aspect_id = db.Column(db.Integer, db.ForeignKey('ItemAspect.id'))


class ItemType(TableMixin, ComponentMixin, TypeMixin, CreationMixin, db.Model):
    items = db.relationship('ItemTypeInventory')


class ItemTypeInventory(TableMixin, db.Model):
    item_id = db.Column(db.Integer, db.ForeignKey('Item.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('ItemType.id'))


class ItemAssociation(TableMixin, ArticleMixin, CreationMixin, db.Model):
    item_1_id = db.Column(db.Integer, db.ForeignKey('Item.id'))
    item_2_id = db.Column(db.Integer, db.ForeignKey('Item.id'))
    types = db.relationship('ItemAssociationTypeInventory')


class ItemAssociationType(TableMixin, ComponentMixin, TypeMixin, CreationMixin, db.Model):
    item_associations = db.relationship('ItemAssociationTypeInventory')


class ItemAssociationTypeInventory(TableMixin, db.Model):
    item_association_id = db.Column(db.Integer, db.ForeignKey('ItemAssociation.id'))
    item_association_type_id = db.Column(db.Integer, db.ForeignKey('ItemAssociationType.id'))


class Event(TableMixin, ArticleMixin, ComponentMixin, CreationMixin, db.Model):
    start = db.Column(db.String)
    end = db.Column(db.String)
    aspects = db.relationship('EventAspect')
    types = db.relationship('EventTypeInventory')


class EventAspect(TableMixin, ArticleMixin, db.Model):
    event_id = db.Column(db.Integer, db.ForeignKey('Event.id'))
    details = db.relationship('EventAspectDetail')


class EventAspectDetail(TableMixin, DetailMixin, db.Model):
    event_aspect_id = db.Column(db.Integer, db.ForeignKey('EventAspect.id'))


class EventType(TableMixin, ComponentMixin, TypeMixin, CreationMixin, db.Model):
    events = db.relationship('EventTypeInventory')


class EventTypeInventory(TableMixin, db.Model):
    event_id = db.Column(db.Integer, db.ForeignKey('Event.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('EventType.id'))


class EventAssociation(TableMixin, ArticleMixin, CreationMixin, db.Model):
    event_1_id = db.Column(db.Integer, db.ForeignKey('Event.id'))
    event_2_id = db.Column(db.Integer, db.ForeignKey('Event.id'))
    types = db.relationship('EventAssociationTypeInventory')


class EventAssociationType(TableMixin, ComponentMixin, TypeMixin, CreationMixin, db.Model):
    event_associations = db.relationship('EventAssociationTypeInventory')


class EventAssociationTypeInventory(TableMixin, db.Model):
    event_association_id = db.Column(db.Integer, db.ForeignKey('EventAssociation.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('EventAssociationType.id'))


class ItemEvent(TableMixin, ArticleMixin, CreationMixin, db.Model):
    item_id = db.Column(db.Integer, db.ForeignKey('Item.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('Event.id'))
    types = db.relationship('ItemEventTypeInventory')


class ItemEventType(TableMixin, ComponentMixin, TypeMixin, CreationMixin, db.Model):
    item_events = db.relationship('ItemEventTypeInventory')


class ItemEventTypeInventory(TableMixin, db.Model):
    item_event_id = db.Column(db.Integer, db.ForeignKey('ItemEvent.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('ItemEventType.id'))


class IntervalType(TableMixin, ComponentMixin, TypeMixin, CreationMixin, db.Model):
    intervals = db.relationship('Interval')


class Interval(TableMixin, ComponentMixin, ArticleMixin, db.Model):
    type_id = db.Column(db.Integer, db.ForeignKey('IntervalType.id'))
    predecessor_count = db.Column(db.Integer)


class Calendar(TableMixin, ComponentMixin, ArticleMixin, CreationMixin, db.Model):
    pass


class CalendarInterval(TableMixin, ArticleMixin, CreationMixin, db.Model):
    interval_id = db.Column(db.Integer, db.ForeignKey('Interval.id'))
    calendar_id = db.Column(db.Integer, db.ForeignKey('Calendar.id'))
