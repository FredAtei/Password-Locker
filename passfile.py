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


class Credentials:
    """
    Class that generates new instances of user Credentials
    """

    Credentials_list = []

    def __init__(self, App, Username, Password):

      # docstring removed for simplicity

        self.App = App
        self.Username = Username
        self.Password = Password
