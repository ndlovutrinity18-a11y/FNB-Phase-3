class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
    @property
    def email(self):
        """Return the user's email address."""
        print("Email Accessed")
        return self._email
    @email.setter
    def email(self, new_email):
        """Set the user's email address."""
        print("Email Updated")
        self._email = new_email

user1 = User("Winny", "winny@gmail.com", "06@Dwinny")
print(user1.email)

user1.email = "winny18@gmail.com"
print(user1.email)