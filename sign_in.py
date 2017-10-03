import csv


class SignIn:
    def __init__(self, email, password):
        self.email = email
        self.__password = password

    def verify_sign_in(self):

        #reading the user details in the csv and spliting it to make a list to get index of email
        with open('user.csv', 'r') as csv_file:
            users = csv.DictReader(csv_file)

            for user in users:
                if self.email == user['email'] and self.password == user['password']:
                    return "Welcome {}".format(user['firstname'])

                elif self.email == user['email'] and self.password != user['password']:
                    return "incorrect password"

                elif self.email != user['email'] and self.password != user['password']:
                    return "incorrect password"

                else:
                    return "Try again"

if __name__ == '__main__':
    email = input("Enter email: ")
    password = input("Enter password: ")
    signin = SignIn(email, password)