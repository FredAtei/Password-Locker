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
