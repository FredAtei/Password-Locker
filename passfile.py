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

    def delete_User(self):
        '''
        delete_User method deletes a saved User account from the User_list
        '''

        User.User_list.remove(self)


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
