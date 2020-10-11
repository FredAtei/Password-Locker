import unittest
from passfile import User
from passfile import Credentials


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

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.User_list), 1)

    def test_display_all_user(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_user(), User.User_list)


if __name__ == '__main__':
    unittest.main()
