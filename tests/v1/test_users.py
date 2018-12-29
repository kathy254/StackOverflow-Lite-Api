#Library imports
import json
from passlib.hash import pbkdf2_sha256 as sha256
import datetime

#Local imports
from .base_tests import BaseTest
from app.api.v1.models.user_models import Accounts

signup_url = 'api/v1/auth/signup'
login_url = 'api/v1/auth/login'
all_members_url = 'api/v1/auth/users'

class TestUser(BaseTest):

    def test_signup(self):
        with self.client:
            signup_payload = {"email_address": "myname@gmail.com", "username": "myname", "password": "abcdefgji"}
            response = self.client.post(signup_url, data=json.dumps(signup_payload), content_type = 'application/json')
            result = json.loads(response.data.decode('UTF-8'))

            self.assertEqual(result["status"], "Success")
            self.assertTrue(result["message"], "User with username myname added successfully")
            self.assertEqual(response.status_code, 201)
            self.assertEqual(result["response"], "Welcome to StackOverflow-Lite")
            self.assertTrue(response.content_type == "application/json")

    def test_existing_username(self):

        with self.client:
            #register user

            register1 = {"email_address": "dontknow@gmail.com", "username": "number1", "password": "isisisisis"}
            self.client.post(signup_url, data = json.dumps(register1), content_type = "application/json")

            #register with existing username
            new_user = {"email_address": "new_user@gmail.com", "username": "number1", "password": "qwertyuiop"}
            response2 = self.client.post(signup_url, data = json.dumps(new_user), content_type = "application/json")
            result3 = json.loads(response2.data.decode("UTF-8"))

            self.assertEqual(result3["status"], "Failed")
            self.assertEqual(result3["message"], "This username already exists. Please choose another one.")
            self.assertEqual(response2.status_code, 500)
            self.assertTrue(response2.content_type == "application/json")


    

    def test_existing_email(self):
        with self.client:
            #register a user
            payload = {"email_address": "someone@gmail.com", "username": "someone", "password": "easyguess"}
            self.client.post(signup_url, data = json.dumps(payload), content_type = "application/json")

            #register user with existing email
            payload3 = {"email_address": "someone@gmail.com", "username": "nobody", "password": "secrets"}
            register3 = self.client.post(signup_url, data = json.dumps(payload3), content_type = "application/json")
            result = json.loads(register3.data.decode("UTF-8"))
            self.assertEqual(result["status"], "Failed")
            self.assertEqual(result["message"], "This email address already exists. Please log in")
            self.assertEqual(register3.status_code, 500)
            self.assertTrue(register3.content_type == "application/json")


    def test_user_login(self):
        with self.client:
            #register new user
            payload4 = {"email_address": "cathy@gmail.com", "username": "cathy", "password": "cathyuser"}
            self.client.post(signup_url, data = json.dumps(payload4), content_type = "application/json")

            #test for successful login
            login_payload = {"username": "cathy", "password": "cathyuser"}
            response4 = self.client.post(login_url, data = json.dumps(login_payload), content_type = "application/json")
            result4 = json.loads(response4.data.decode("UTF-8"))


            self.assertEqual(result4["status"], "OK")
            self.assertEqual(result4["message"], "Welcome cathy. You have logged in successfully")
            self.assertTrue(result4["token"])
            self.assertEqual(response4.status_code, 200)
            self.assertTrue(response4.content_type == "application/json")

            #test user not found
            incorrect_payload = {"username": "faith", "password": "faithuser"}
            response5 = self.client.post(login_url, data = json.dumps(incorrect_payload), content_type = "application/json")
            result5 = json.loads(response5.data.decode("UTF-8"))

            self.assertEqual(result5["status"], "Failed")
            self.assertEqual(result5["message"], "User does not exist")
            self.assertEqual(response5.status_code, 200)
            self.assertTrue(response5.content_type == "application/json")

            #test incorrect password
            incorrect_password = {"username": "cathy", "password": "incorrect"}
            response6 = self.client.post(login_url, data = json.dumps(incorrect_password), content_type = "application/json")
            result6 = json.loads(response6.data.decode("UTF-8"))

            self.assertEqual(result6["status"], "Failed")
            self.assertEqual(result6["message"], "Password is incorrect. Please try again.")
            self.assertEqual(response6.status_code, 400)
            self.assertTrue(response6.content_type == "application/json")


    def test_encode_token(self):
        user = {"email_address": "new_email@gmail.com", "username": "new_email", "password": "password5"}
        token = Accounts.encode_login_token(user["username"], user["password"])
        self.assertTrue(isinstance(token, bytes))


    def test_decode_token(self):
        user2 = {"username": "currentuser", "password": "userpassword"}
        token2 = Accounts.encode_login_token(user2["username"], user2["password"])
        self.assertTrue(isinstance(token2, bytes))
        self.assertTrue(Accounts.decode_auth_token(token2)["username"] == "currentuser")
        self.assertTrue(Accounts.decode_auth_token(token2)["password"] == "userpassword")


    def test_get_all_users(self):
        with self.client:
            payload5 = {"email_address": "another_user@gmail.com", "username": "another_user", "password": "anotheruser"}
            token = Accounts.encode_login_token(payload5["username"], payload5["password"])
            self.client.post(signup_url, data = json.dumps(payload5), content_type = "application/json")
            response7 = self.client.get(all_members_url, headers = {"X-API-KEY": "{}".format(token)})
            self.assertEqual(response7.status_code, 200)


    