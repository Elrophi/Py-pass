import pyperclip
import random


class User:
    '''
    create and save user details
    '''

    users_list = []
    def __init__(self, f_name,l_name,password):
        '''
        defining properties to hold user objects
        '''

        self.f_name = f_name
        self.l_name = l_name
        self.password = password

    def save_user_info(self):
        '''
        save new created user instances
        '''
        User.users_list .append(self)


class Details:
    '''
    create account details, paswords and save details
    '''

    details_list = []
    user_details_list = []

    @classmethod
    def check_user(cls,f_name,password):
        '''
        check if name and password matches any entry in the list
        '''
        current_user = ''
        for user in User.users_list:
            if (user.f_name == f_name and user.password == password):
                current_user = user.f_name
        return current_user


