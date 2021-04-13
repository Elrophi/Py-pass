import unittest
import pyperclip
from user_details import User, Details


class TestUser(unittest.TestCase):
    '''
    defining test cases for user
    Args:
        unittest.TestCase: it creates test cases
    '''
    def setUp(self):
        '''
        user account setup for testing each case
        '''
        self.n_user = User('Ben','Jackson','test01')

    # Test one
    def test__init__(self):
        '''
        test to check if user instances created follows the rule set
        '''
        self.assertEqual(self.n_user.f_name,'Ben')
        self.assertEqual(self.n_user.l_name,'Jackson')
        self.assertEqual(self.n_user.password,'test01')

    # Test two
    def test_save(self):
        '''
        Check if user details is saved
        '''
        self.n_user.save_user_details()
        # self.assertEqual(len(User.users_list),1)

class TestDetails(unittest.TestCase):
    '''
    test for user credentials

    Args:
        unittest.TestCase: it creates test cases
    '''

    # Test three
    def test_check_user(self):
        '''
        checking if the user credentials works
        '''
        self.n_user = User('Ben','Jackson','test01')
        self.n_user.save_user_details()

        user2 = User('Joe','Jackson','test01')
        user2.save_user_details()

        for user in User.users_list:
            if user.f_name == user2.f_name and user.password == user2.password:
                current_user = user.f_name
        return current_user

        self.assertEqual(current_user,Details.check_user(user2.password,user2.f_name))


    def setUp(self):
        '''

        '''
        self.new_details = Details('Ben','Instagram','Benny','test01')

    def tearDown(self):
        '''

        '''
        Details.details_list = []
        User.users_list = []

    # Test four
    def test__init__(self):
        self.assertEqual(self.new_details.username, 'Ben')
        self.assertEqual(self.new_details.site, 'Instagram')
        self.assertEqual(self.new_details.account, 'Benny')
        self.assertEqual(self.new_details.password, 'test01')

    
    # Test five
    def test_save_details(self):
        '''

        '''
        self.new_details.save_details()
        facebook = Details('Joe','Facebook','Benny','test01')
        facebook.save_details()
        self.assertEqual(len(Details.details_list),2)

    
    # Test six
    def test_display_details(self):
        '''

        '''
        self.new_details.save_details()
        facebook = Details('Ben','Facebook','Benny','test01')
        facebook.save_details()
        twitter = Details('Ben','Twitter','Benny','test01')
        twitter.save_details()
        # self.assertEqual(len(Details.display_details(facebook.username)),2)

    # Test seven
    def test_find_by_site_name(self):
        '''

        '''
        self.new_details.save_details()
        facebook = Details('Ben','Facebook','Benny','test01')
        facebook.save_details()
        details_exists = Details.find_by_site_name('Facebook')
        self.assertEqual(details_exists,facebook)


    # Test eight
    def test_copy_details(self):
        '''

        '''
        self.new_details.save_details()
        facebook = Details('Ben','Facebook','Benny','test01')
        facebook.save_details()
        find_details = None
        for details in Details.user_details_list:
            find_details=Details.find_by_site_name(details.site)
            return pyperclip.copy(find_details.password)
        Details.copy_details(self.new_details.site)
        self.assertEqual('test01',pyperclip.paste())
        print(pyperclip.paste())



if __name__ == '__main__':
    unittest.main()