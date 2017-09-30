import time
import datetime

class SignUp:


    def __init__(self, firstname, lastname, email, password, birthday, gender):

        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.birthday = birthday
        self.gender = gender

    def choose_birthday(self):

     date = int(self.birthday)
     self.birthday = datetime.date(date)


     def __repr__(self):
        return self.firstname or self.lastname

user1 = SignUp("Anty", "Tope", "tope@gmail.com", "aasmdmdmj", "25jan", "female")
print(user1)
user1 = SignUp("Anty", "Tope", "tope@gmail.com", "aasmdmdmj", "25jan", "female")
print(user1)