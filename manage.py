from multiprocessing import managers
from app import create_app
from flask_script import Manager,Server

#create app instance
app=create_app('development')

#instanciate Manager class
manager=Manager(app)
manager.add_command('server',Server)
#command "server" will launch our app server

@manager.command
def test():
    #run unit tests
    import unittest
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__=='__main__':
    manager.run()