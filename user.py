import csv
import os


class User:
    def __init__(self, firstname='', lastname='', email='', password='', birthday='', gender=''):

        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.birthday = birthday
        self.gender = gender

    def __repr__(self):
        return "Welcome", self.firstname

    def save_to_csv(self):

        # create a csv file that contains users content
        file_exist = os.path.isfile('user.csv')
        with open('user.csv', 'a') as csv_file:
            fieldnames = ['firstname', 'lastname', 'email', 'password', 'birthday', 'gender']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if not file_exist:
                writer.writeheader()
            writer.writerow(
                {'firstname': self.firstname, 'lastname': self.lastname, 'email': self.email, 'password': self.password,
                 'birthday': self.birthday, 'gender': self.gender})

    def verify_email(self):

        # reading the user details in the csv and spliting it to make a list to get index of email
        with open('user.csv', 'r') as csv_file:
            users = csv.DictReader(csv_file)

            for user in users:
                if self.email == user['email'] and user['password']:
                    return 'Sorry email already exist'
                else:
                    return 'Welcome {}'.format(self.firstname)



                    # for user in csv_file:
                    #     stored_email = user.split(",")[2]
                    #     #user.split[2] get the index of email in the csv file
                    #
                    #     if stored_email == self.email:
                    #         return "email already exist"
                    #     else:
                    #         return "successfully registered"


if __name__ == "__main__":
    pass
    # new = User()
    # new.save_to_csv()
    # print(new.verify_email("abc@gmail"))
