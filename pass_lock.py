import pyperclip
from user_details import User, Details


def new_user(fname,lname,password):
    '''
    create new user
    '''
    n_user = User(fname,lname,password)
    return n_user

def save_user(user):
    '''
    save new user account
    '''
    User.save_user_details(user)

def verify_user(fname,password):
    '''
    verify if there is already a user before adding details
    '''

    check_user = Details.check_user(fname,password)
    return check_user

def new_password():
    '''
    automatic random password generator
    '''
    passcode = Details.new_password()
    return passcode

def create_detail(username,site,account,password):
    '''
    create new user details
    '''
    new_details=Details(username,site,account,password)
    return new_details

def save_details(details):
    '''
    save newly created detail
    '''
    Details.save_details(details)

def display_details(username):
    '''
    display saved user details
    '''
    return Details.display_details(username)

def copy_details(site):
    '''
    copy all details to clipboard
    '''
    return Details.copy_details(site) 


def main():
    print("Welcome to PY-Password-Locker")
    while True:
        print('*'*40)
        print("Select task to execute\n ca-Create Account \n l-Log In\n ex-Exit")
        options = input().lower().strip()

if __name__ == '__main__':
    main()   

