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


class testCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    '''

    def setUp(self):

        self.new_credential = Credentials(
            "Instagram", "Fred", "a1B2c3D4e")

    def test_init(self):

        self.assertEqual(self.new_credential.App, 'Instagram')
        self.assertEqual(self.new_credential.Username, 'Fred')
        self.assertEqual(self.new_credential.Password, 'a1B2c3D4e')

    def save_credential_test(self):

        self.new_credential.save_info()
        self.assertEqual(len(Credentials.Credentials_list), 1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.Credentials_list = []

# other test cases here
    def test_save_multiple_Credentials(self):

        self.new_credential.save_info()
        test_Credentials = Credentials("Instagram", "Fred",
                                       "a1B2c3D4e")  # new contact
        test_Credentials.save_info()
        self.assertEqual(len(Credentials.Credentials_list), 2)

    def test_delete_credentials(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_credential.save_info()
        test_Credentials = Credentials("Instagram", "Fred",
                                       "a1B2c3D4e")  # new contact
        test_Credentials.save_info()

        self.new_credential.delete_credentials()  # Deleting a contact object
        self.assertEqual(len(Credentials.Credentials_list), 1)

    def test_find_credentails(self):
        '''
        test to check if we can find a credentials and display information
        '''

        self.new_credential.save_info()
        test_Credentials = Credentials("Instagram", "Fred",
                                       "a1B2c3D4e")  # new credentials
        test_Credentials.save_info()

        found_credential = Credentials.find_credentials("Instagram")

        self.assertEqual(found_credential.App, test_Credentials.App)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credential.save_info()
        test_Credentials = Credentials("Instagram", "Fred",
                                       "a1B2c3D4e")  # new credentials
        test_Credentials.save_info()

        credentials_exists = Credentials.credentials_exist("Instagram")

        self.assertTrue(credentials_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),
                         Credentials.Credentials_list)


if __name__ == '__main__':
    unittest.main()
