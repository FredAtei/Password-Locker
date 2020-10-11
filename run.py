#!/usr/bin/env python3.6
from passfile import User
from passfile import Credentials


def create_User(Username, Password):
    '''
    Function to create a new contact
    '''
    new_User = User(Username, Password)
    return new_User


def save_User(User):
    '''
    Function to save contact
    '''
    User.save_User()


def del_User(User):
    '''
    Function to delete a contact
    '''
    User.delete_User()
