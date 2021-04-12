import pyperclip
from user_details import User, Details


def new_user(fname,lname,password):
    '''
    create new user
    '''
    n_user = User(fname,lname,password)
    return n_user


    

