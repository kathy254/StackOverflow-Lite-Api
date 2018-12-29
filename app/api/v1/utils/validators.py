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


    def is_signup_payload(self, items):
        res = self.payload(items, 3, ['email_address', 'username', 'password'])
        return res


    @staticmethod
    def is_valid_email(email_address):
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_address) is None:
            res = True
        else:
            res = False
        return res

    
    @staticmethod
    def is_valid_password(password):
        if (len(password)<6) is True:
            res = True
        else:
            res = False
        return res


    def is_login_payload(self, items):
        res = self.payload(items, 2, ['username', 'password'])
        return res


    @staticmethod
    def list_iterator(list):
        for i in list:
            if i is None or not i:
                return False