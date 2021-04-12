import pyperclip
import random
import string



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

    def __init__(self,username,site,account,password):
        '''
        defining properties for each usser object
        '''

        self.username = username
        self.site = site
        self.account = account
        self.password = password

    def save_details(self):
        '''
        saving new created user
        '''
        Details.details_list.append(self)
    # use of import string
    def new_password(char = string.ascii_letters + string.punctuation + string.digits):
        '''
        generate new password for user
         _ means ignore the index
         '''
        passcode = "".join(random.choice(char) for _ in range(random.randint(8, 16)))
        return passcode

    @classmethod
    def display_details(cls,username):
        '''
        class method to display the details list
        '''
        user_details_list = []
        for details in cls.details_list:
            if details.username == username:
                user_details_list.append(details)
        return user_details_list


    @classmethod
    def find_by_site_name(cls,site):
        '''
        checks site name and returns user details
        '''
        for details in cls.details_list:
            if details.site == site:
                return details

    @classmethod
    def copy_details(cls,site):
        '''copy user deails 
        '''
        find_details = Details.find_by_site_name(site)
        return pyperclip.copy(find_details.password)



