import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    def setUp(self):
        #create an instance of User class
        self.new_user=User(password='banana')

    def test_password_setter(self):
        #test case to check if password is being hashed and pass_secure has a value
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        #confirm that app aises atribute error when we try to access password property
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        #test that password hash can be verified when we pass in correct password
        self.assertTrue(self.new_user.verify_password('banana'))