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
    User.save_user()


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
    new_credentials = Credentials(App, Username, Password)
    return new_credentials


def save_info(credentials):
    '''
    Function to save contact
    '''
    credentials.save_info()


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


def generate_Password():
    '''
    generates a random password for the user.
    '''
    gen_password = Credentials.generatePassword()
    return gen_password


def main():
    print("Hello, Welcome to your Password Locker. Use these short codes:...\n Signin or Signup by choosing the following \n si ---  Have An Account(signin)  \n su ---  Create New Account(signup)  \n")
    short_code = input("").lower().strip()
    if short_code == "su":
        print("SignUp")
        print('-' * 100)
        Username = input("User_name: ")

        while True:
            print(" ep - Enter your password:\n gp - Select to generate a Password")
            Password_Choice = input().lower().strip()
            if Password_Choice == 'ep':
                Password = input("Enter your password\n")
                break
            elif Password_Choice == 'gp':
                Password = generate_Password()
                break
            else:
                print("Wrong password. Try again.")
        save_user(create_user(Username, Password))
        print("-"*100)
        print(
            f"Welcome {Username}, Account has been created. Your password is: {Password}")
        print("-"*100)

    elif short_code == "si":
        print("-"*100)
        print("Use your Account and Password to log in:")
        print('*' * 50)
        Username = input("User name: ")
        Password = input("password: ")
        signin = signin_user(Username, Password)
        if signin_user == signin:
            print(f"Welcome {Username}.")
            print('\n')

    while True:
        print("Use these short codes to procceed:\n cc - Create new credential \n dc - Display Credentials \n fc - Find Credentials \n gp - Generate A randomn password \n de - Delete credential \n ex - Exit this App \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("-"*30)
            print("Name of Application Account ....")
            App = input().lower()
            print("Your App Username")
            Username = input()

            while True:
                print(
                    " ep - Enter password for existing app account:\n gp - To generate Password")
                Password_Choice = input().lower().strip()
                if Password_Choice == 'ep':
                    Password = input("Enter your password\n")
                    break
                elif Password_Choice == 'gp':
                    Password = generate_Password()
                    break
                else:
                    print("Wrong password. Try again.")
            save_info(create_credentials(
                App, Username, Password))
            print('\n')
            print(
                f"Account Credentials for: {App} - Username: {Username} - Password:{Password} has been created")
            print('\n')

        elif short_code == "dc":
            if display_credentials():
                print("All App Credentials: ")

                print('-' * 30)
                print('-' * 30)
                for App in display_credentials():
                    print(
                        f" App:{App.App} \n Username:{Username}\n Password:{Password}")
                    print('-' * 30)
                print('-' * 30)
            else:
                print("There is no credential to be displayed.")
        elif short_code == "fc":
            print("Enter the App to find credentials")
            Search_app = input().lower()
            if find_credentials(Search_app):
                search_credential = find_credentials(Search_app)
                print(f"App Name : {search_credential.App}")
                print('-' * 40)
                print(
                    f"Username: {search_credential.Username} Password :{search_credential.Password}")
                print('-' * 40)
            else:
                print("Credential cannot be found")
                print('\n')

        elif short_code == 'gp':

            password = generate_Password()
            print(
                f" {password} has been generated succesfull.")
        elif short_code == 'ex':
            print("Exiting App.. See you Soon!")
            break
        else:
            print(
                "Error... Please select entry provided")
    else:
        print("Please enter a valid input to continue")


if __name__ == '__main__':

    main()
