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

    def delete_contact(self):
        '''
        delete_contact method deletes a saved User account from the User_list
        '''

        User.User_list.remove(self)


class Credentials:
    """
    Class that generates new instances of user Credentials
    """

    Credentials_list = []

    # @classmethod
    # def verify_user(cls, username, password):
    #     """
    #     method to verify whether the user is in our user_list or not
    #     """
    #     a_user = ""
    #     for user in User.User_list:
    #         if(user.username == username and user.password == password):
    #             a_user == user.username
    #     return a_user

    def __init__(self, App, Username, Password):

      # docstring removed for simplicity

        self.App = App
        self.Username = Username
        self.Password = Password

    def save_info(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.Credentials_list.append(self)
