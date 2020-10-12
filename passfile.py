import random
import string


class User:
    """
    Class that generates new instances of the User
    """

    User_list = []

    def __init__(self, Username, Password):

      # docstring removed for simplicity
        self.Username = Username
        self.Password = Password

    def save_user(self):
        '''
        save_contact method saves contact objects into contact_list
        '''

        User.User_list.append(self)

    @classmethod
    def display_user(cls):
        '''
        method that returns the contact list
        '''
        return cls.User_list

    def delete_user(self):
        '''
        delete_User method deletes a saved User account from the User_list
        '''

        User.User_list.remove(self)


class Credentials:
    """
    Class that generates new instances of user Credentials
    """

    Credentials_list = []

    @classmethod
    def true_user(cls, Username, Password):
        """
        method to confirm the user in the app
        """
        the_user = ""
        for Username in User.User_list:
            if(Username.username == Username and Username.Password == Password):
                the_user == Username.username
        return the_user

    def __init__(self, App, Username, Password):

      # docstring removed for simplicity

        self.App = App
        self.Username = Username
        self.Password = Password

    def save_info(self):
        '''
        save info allows to save details of the credentials we add
        '''

        Credentials.Credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved info from the credentials_list
        '''

        Credentials.Credentials_list.remove(self)

    @classmethod
    def find_credentials(cls, App):
        '''
        Method that takes in a Application and returns a credential that matches that Apllication.

        Args:
            App: Application to search for
        Returns :
            Credentials of person that matches the App.
        '''

        for Credentials in cls.Credentials_list:
            if Credentials.App == App:
                return Credentials

    @classmethod
    def credentials_exist(cls, App):
        '''
        Method that checks if a Credentials exists from the credential list.
        Args:
            App: Application to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for Credentials in cls.Credentials_list:
            if Credentials.App == App:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the Credentials list
        '''
        return cls.Credentials_list
