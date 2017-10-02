import sign_up
import user
import csv


class SignIn:

    def __init__(self, email, password):

        self.email = email
        self.password = password

    def verify_sign_in(self):

        #reading the user details in the csv and spliting it to make a list to get index of email
        with open('user.csv', 'r') as csv_file:
            for user in csv_file:
                stored_email = user.split(",")[2]
                # user.split[2] get the index of email in the csv file

                if stored_email == self.email:
                    return "welcome", self.firstname
                else:
                    return "wrong email"


if __name__ == "__main__":
    old = SignIn("abc", "wwwww")
    old.verify_sign_in()



