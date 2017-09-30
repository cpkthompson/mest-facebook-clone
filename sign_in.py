import sign_up.py

class SignIn:

    def __init__(self, email, password):

        self.email = email
        self.password = password

    def invalid_password(self):

        if self.email != SignUp(self.email):
            return "invalid password"



