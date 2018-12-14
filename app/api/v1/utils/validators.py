from flask import abort

import re

class Verify:
    def is_empty(self, items):
        for item in items:
            if bool(item) is False:
                return True
        return False


    def is_whitespace(self, items):
        for item in items:
            if item.isspace() is True:
                return True
        return False


    def payload(self, items, length, keys):
        items = items.keys()
        if len(items) == length:
            for item in items:
                if item not in keys:
                    return False
                return True
        else:
            return False


    def is_signup_payload(self, items):
        result = self.payload(items, 3, ['email_address', 'username', 'password'])
        return result


    def is_valid_email(self, email_address):
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_address.islower()):
            Message: "Invalid email address"
            abort(400, Message)

    
    def is_valid_password(self, password):
        if len(password) < 6 or len(password) > 12:
            Message: "Password must be longer than 6 characters and less than 12 characters"
            abort(400, Message)


    def is_login_payload(self, items):
        result = self.payload(items, 2, ['username', 'password'])
        return result