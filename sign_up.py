import user
import sign_in


class SignUp():
    def __init__(self, firstname, lastname, email, password, birthday, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.birthday = birthday
        self.gender = gender
        self.check_email()

    def create_new_user(self):
        new_user = user.User(self.firstname, self.lastname, self.email, self.password, self.birthday, self.gender)
        new_user.save_to_csv()

    def check_email(self):
        with open('user.csv', 'r') as csv_file:
            all_users = csv.DictReader(csv_file)

            for user in users:
                if self.email == user['email']:
                    print('Sorry this email is already taken')
                    # run questions
                else:
                    self.create_new_user()

