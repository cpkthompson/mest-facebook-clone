import os.path
import datetime
import csv


class Users:

    def __init__(self, users = []):
        self.users = users

    def users_list(self, user):
        self.users.append(user)

    def create_csv(self, user):

        file_exist = os.path.isfile('user.csv')
        with open('user.csv', 'a') as csv_file:
            fieldnames = ['firstname', 'lastname', 'email', 'password', 'birthday', 'gender']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if not file_exist:
                writer.writeheader()
            writer.writerow(
                {'firstname': user.firstname, 'lastname': user.lastname, 'email': user.email, 'password': user.password, 'birthday': user.birthday, 'gender': user.gender})


class SignUp:

    def __init__(self, firstname ='', lastname ='', email ='', password ='', birthday ='', gender =''):

        self.firstname = input("Enter your firstname: ")
        self.lastname = input("Enter your lastname: ")
        self.email = input("Enter your email: ")
        self.password = input("Enter your password: ")
        self.birthday = input("Enter your birthday: ")
        self.gender = input("Enter your gender: ")


class SignIn:

    def __init__(self, email ='', password =''):

        self.email = input("Enter your email: ")
        self.password = input("Enter your password: ")

    def verify_sign(self, user):

        if self.email == SignUp(user.email):
            print("Successful")

        else:
            self.email != user.email
            print("invalid email")


def main():

    while True:
        new_user = Users()
        register = int(input('Type 1 to sign up as a new user, 2 to sign in: '))

        if register == 1:
            user = SignUp()
            new_user.users_list(user)
            new_user.create_csv(user)

        elif register == 2:
            user = SignIn()
            new_user.verify_sign(user)

        else:
            print("End here")
            break

main()
