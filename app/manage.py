import os
import unittest
import glob
import json

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
from app.main.model import model

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command
def seed():
    from app.main.model.model import ItemType

    item_type_files = glob.iglob('../data/ItemType_*.json')

    for f in item_type_files:
        with open(f, encoding = 'utf-8-sig') as json_data:
            item_types = ItemType(json.loads(json_data.read()))

        db.session.add(item_types)
        db.session.commit()

if __name__ == '__main__':
    manager.run()