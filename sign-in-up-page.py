from sign_in import SignIn
from sign_up import SignUp

class SignInUpPage():
    def __init__(self, register):
        self.register = register

        if self.register == 1:
            SignIn(email, password)

        elif self.register == 2:
            SignUp(firstname, lastname, email, birthday, gender, password)

        else:
            print("You didn't enter a correct value.")


if __name__ == '__main__':
    register = input("Type 1 to Sign In or 2 to Sign Up: ")

    if register == 1:
        email = input("Please enter your email: ")
        password = input("Please enter your password: ")

    elif register == 2:
        firstname = input("Please enter your firstname : ")
        lastname = input("Please enter your lastname: ")
        email = input("Please enter your email: ")
        birthday = input("Please enter your birthday : ")
        gender = input("Please enter your gender (M or F) : ")
        password = input("Please enter your password: ")

    new_session = SignInUpPage(register)