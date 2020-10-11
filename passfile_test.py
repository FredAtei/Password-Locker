import unittest
from passfile import User


class TestUser (unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Fred", "a1B2c3D4e")  # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.Username, "Fred")
        self.assertEqual(self.new_user.Password, "a1B2c3D4e")


if __name__ == '__main__':
    unittest.main()
