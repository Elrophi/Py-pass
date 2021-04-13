import unittest
import pyperclip
from user_details import User, Details


class TestUser(unittest.TestCase):
    '''
    defining test cases for user
    Args:unittest.TestCase: it creates test cases
    '''
    def user(self):
        '''
        user account setup for testing each case
        '''
        self.n_user = User('Ben','Jackson','test01')

    def test__init__(self):
        '''
        test to check if user instances created follows the rule set
        '''
        self.assertEqual(self.n_user.f_name,'Ben')
        self.assertEqual(self.n_user.l_name,'Jackson')
        self.assertEqual(self.n_user.password,'test01')

    def test_save(self):


if __name__ == '__main__':
    unittest.main()