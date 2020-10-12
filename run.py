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
    new_credentials = Credentials(App, Username, Password)
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


def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password = Credentials.generatePassword()
    return auto_password


def main():
    print("Hello Welcome to your Password Manager. What is your name?")
    user_name = input("Your Name:")

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Please use these short codes : cc - create credential,dc- display Credential, lo - login, fa -find account,del- delete Credential, ex -exit the account list")

        short_code = input().lower()

        if short_code == 'cc':

            print("Enter a Username For Password Manager to get started:")
            username = input()

            print("Enter a Password For Password Manager to get started:")
            password = input()

            save_credentials(create_credentials(Username, Password))
            print('\n')
            print(
                f"Your Username: {Username}, password: {Password} credentials have been saved")
            print('\n')

        elif short_code == 'lo':
            print('Please Note inorder for you to login you must have a credentials account with Password Manager saved for you to use the Login option! Thankyou.')
            print('Enter your Credentials for Password Manager to proceed :')
            print("-"*10)

            print("Username:")
            username = input()

            print("Password:")
            password = input()

            information = authenticate_details(username, password)
            if information == 0:
                print("\n")
                print("Sorry, Your username or password for Password manager is invalid")

            elif information != 0:
                print('\n')
                print(
                    f"Hello again {information.username}, What do you want to do today?")
                print('\n')

                while True:
                    print("Please use short codes for faster service: cc - Create a new account, co - Copy to clipboard, dc - display credential, ex - exit account list:")
                    short_code = input().lower()
                    if short_code == 'cc':
                        print('Create Account Option:')

                        print("Account Name:")
                        account_name = input()

                        print("Username:")
                        username = input()

                        print('PLease dictate the length of your password')
                        length = int(input())
                        password = generate_user_password(length)
                        print(
                            f"Password Manager is recommending {password} for your {account_name} account!")
                        save_account(create_account(
                            account_name, username, password))

                    elif short_code == 'dc':
                        if display_accounts():
                            print('Here is a list of all user accounts')
                            print('\n')

                            for account in display_accounts():
                                print(
                                    f"The Account {account.account_name} has a username of {account.username} and the password is {account.password}")
                                print('\n')

                        else:
                            print('\n')
                            print(
                                f'You dont seem to have any new credentials, {information.username}')
                            print('\n')

                    elif short_code == 'ex':
                        print(
                            "Thankyou for using Password Manager, you have exited your user-account list!")
                        break

        elif short_code == 'dc':

            if display_credentials():
                print("Here is a list of all credentials")
                print('\n')

                for credential in display_credentials():
                    print(f"Username: {credential.username}. ")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any credentials saved yet")
                print('\n')

        elif short_code == 'fa':

            print("Enter the Credential you want to search for")

            search_credential = input()
            if account_exist(search_credential):

                search_for_credential = find_credential(search_credential)
                print(
                    f"This Account {search_for_credential.username} exists with the password {search_for_credential.password} ")
                print('-' * 20)

            else:
                print("That credential does not exist")

        elif short_code == 'del':

            print("Enter the Credential you want to delete")

            searching_credential = input()
            if account_exist(searching_credential):
                search_cred = find_credential(searching_credential)
                search_cred.delete_credential()
                print(
                    f"This Account  {search_cred.username} has been deleted!")
                print('-' * 20)

            else:
                print("That credential does not exist")

        elif short_code == "ex":
            print("You have exited the credential list, Have a Nice day!")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
