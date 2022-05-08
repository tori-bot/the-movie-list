
from app import create_app,db
from flask_script import Manager,Server
from app.models import Role, User,Review
from flask_migrate import Migrate,MigrateCommand

#create app instance
app=create_app('production')

#instanciate Manager class
manager=Manager(app)
manager.add_command('server',Server)
#command "server" will launch our app server

#initiate migrate class and pass in app and db instance
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    #funtion allows me to pass in some properties into my shell
    return dict(app=app,db=db,User=User,Role=Role)

@manager.command
def test():
    #run unit tests
    import unittest
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__=='__main__':
    manager.run()