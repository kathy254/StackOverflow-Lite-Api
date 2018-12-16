from ..utils.validators import Verify

user_accounts = []


class Accounts(Verify):
    '''A class to represent the user model'''


    def signup(self, email_address, username, password, timestamp):
        '''method to add a user to user_accounts list'''
        new_member = dict(
            email_address = email_address,
            username = username,
            password = password,
            timestamp = timestamp
        )
        
        member_info = [email_address, username, password]
    
        present = self.list_iterator(member_info)
        if present is False:
            return {"message": "Please fill out all fields"}
        if self.is_signup_payload is False:
            return {"message": "Payload is invalid"}
        if self.is_valid_password(password) is True:
            return {"message": "Password has to be between 6 and 12 characters long"}
        if self.is_valid_email(email_address) is True:
            return {"message": "Please enter a valid email address"}
        else:
            user_accounts.append(new_member)
            return {
                "message": "User with username {} added successfully".format(username),
                "response": "Welcome to StackOverflow-Lite",
                "Stackoverflow member since": timestamp 
                }


    def get_all_users(self):
        if len(user_accounts) == 0:
            return {"message": "No users found"}
        else:
            return user_accounts
        
    def get_single_user(self, username):
        '''method to get user by username'''
        
        single_user = [user for user in user_accounts if user['username'] == username]
        if single_user:
            return single_user[0]
        else:
            return "User not found"