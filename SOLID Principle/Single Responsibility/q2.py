# class User:
#     def login(self):
#         pass
#
#     def register(self):
#         pass
#
#     def send_welcome_email(self):
#         pass
#
#     def save_user(self):
#         pass

# answer

class User:
    def __init__(self,data):
        self.data = data
        self.user_id = self.data['user_id']
        self.user_email = self.data['user_email']
        self.user_password = self.data['user_password']

class UserLogin:
    def login(self,user:User):
        return f"User is logged in"

class UserRegister:
    def register(self,user:User):
        return f"User is registered with user_id {user.user_id}"

class UserSendMail:
    def send(self,user:User):
        return f"User is sent mail to {user.user_email}"

class SaveUser:
    def save(self,user:User):
        return f"User is saved to user_id {user.user_id} and user_email {user.user_email}"
