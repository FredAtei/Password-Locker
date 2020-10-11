#!/usr/bin/env python3.6
from passfile import User
from passfile import Credentials


def create_user(Username, Password):
    '''
    Function to create a new contact
    '''
    new_User = User(Username, Password)
    return new_User


def save_user(User):
    '''
    Function to save contact
    '''
    User.save_User()


def del_user(User):
    '''
    Function to delete a contact
    '''
    User.delete_User()


def signin_user(Username, Password):
    """
    function that checks whether a user exist and then login the user in.
    """
    confirm_user = Credentials.true_user(Username, Password)
    return confirm_user


def create_credentials(App, Username, Password):
    '''
    Function to create new credentails
    '''
    new_credentials = Credentials(Username, Username, Password)
    return new_credentials


def save_credentials(credentials):
    '''
    Function to save contact
    '''
    credentials.save_credentials()


def del_credentials(credentails):
    '''
    Function to delete a contact
    '''
    credentails.delete_credentials()


def find_credentials(App):
    '''
    Function that finds a credential by App and returns the credential
    '''
    return Credentials.find_credentials(App)


def check_credentials(App):
    '''
    Function that check if a credential exists with that app and return a Boolean
    '''
    return Credentials.credentials_exist(App)


def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_credentials()
