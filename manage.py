import os
from app import create_app, db
from flask_script import Manager, Shell
# from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
  return dict(app=app, db=db)

manager.add_command('shell', Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()
