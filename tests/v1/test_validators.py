import unittest

from app.api.v1.utils.validators import Verify

class TestValidators(unittest.TestCase):
    def setUp(self):
        self.data = Verify()


    def tearDown(self):
        self.data = None


    def test_empty_data(self):
        '''method to test if data is empty'''
        test = self.data.is_empty(["", "abcd"])
        self.assertTrue(test)


    def test_is_not_empty(self):
        '''method to test if data is not empty'''
        test = self.data.is_empty(["abcd", "efgh"])
        self.assertFalse(test)

    
    def test_whitespaces(self):
        '''method to test if input has whitespaces'''
        test = self.data.is_whitespace([" ", "ds"])
        self.assertTrue(test)


    def test_no_whitespaces(self):
        '''method to test if input does not have whitespaces'''
        test = self.data.is_whitespace(["ab", "cd"])
        self.assertFalse(test)


    def test_correct_signup_payload(self):
        '''method to verify that signup payload is correct'''
        payload = {"email_address": "email@gmail.com", "username": "user1", "password": "abcd"}
        test = self.data.is_signup_payload(payload)
        self.assertTrue(test)


    def test_incorrect_signup_payload(self):
        '''method to test incorrect signup payload'''
        payload1 = {"email_address": "abc@gmail.com", "myname": "name"}
        payload2 = {"email": "abc@gmail.com", "password": "abcd"}
        payload3 = {"email_address": "efgh@gmail.com"}
        test1 = self.data.is_signup_payload(payload1)
        test2 = self.data.is_signup_payload(payload2)
        test3 = self.data.is_signup_payload(payload3)
        self.assertFalse(test1)
        self.assertFalse(test2)
        self.assertFalse(test3)


    def test_valid_email(self):
        '''method to check for validity of email address'''
        test1 = self.data.is_valid_email("abcd@gmail.com")
        test_ccTLD = self.data.is_valid_email("efgh@gmail.co.ke")
        test_long_TLD = self.data.is_valid_email("ijkl@gmail.travel")
        test_uppercase = self.data.is_valid_email("ABDCDEF@GMAIL.COM")
        self.assertFalse(test1)
        self.assertFalse(test_ccTLD)
        self.assertFalse(test_long_TLD)
        self.assertFalse(test_uppercase)


    def test_invalid_email(self):
        '''method to check for invalid email address'''
        test1 = self.data.is_valid_email("lslslslsl")
        test2 = self.data.is_valid_email("abcdef.com")
        self.assertTrue(test1)
        self.assertTrue(test2)


    def test_valid_password(self):
        '''method to check for valid password'''
        test1 = self.data.is_valid_password("isisisis")
        test2 = self.data.is_valid_password("ISISISIS")
        self.assertFalse(test1)
        self.assertFalse(test2)


    def test_invalid_password(self):
        '''method to check for invalid password'''
        test1 = self.data.is_valid_password("abc")
        test2 = self.data.is_valid_password("akskskskskskskkssksksksksksksksk")
        self.assertTrue(test1)
        self.assertTrue(test2)


    def test_login_payload(self):
        '''method to check for valid login payload'''
        payload = {"username": "myname", "password": "abcdefgh"}
        test = self.data.is_login_payload(payload)
        self.assertTrue(test)


    def test_incorrect_login_payload(self):
        '''method to check for incorrect login payload'''
        payload1 = {"email_address": "abcd@gmail.com"}
        payload2 = {"user": "myname", "pass": "notpass"}
        test = self.data.is_login_payload(payload1)
        test2 = self.data.is_login_payload(payload2)
        self.assertFalse(test)
        self.assertFalse(test2)

    



