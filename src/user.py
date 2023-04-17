class User:
    def __init__(self):
        self.userData = self.parseUserData()

    def parseUserData(self):
        userData = {}
        columns = ["first name", "last name", "date of birth", "email", "phone number"]
        for column in columns:
            userData[column] = input(f"What's your {column}? ")
        return userData
