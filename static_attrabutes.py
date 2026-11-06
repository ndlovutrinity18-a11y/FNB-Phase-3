class User:
    user_count = 0  # Class attribute to keep track of the number of users
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1
        
    def display_user(self):
        print(f"Username: {self.username}, Email {self.email}")
        
user1 = User("Winny","winny18@gmail.com")
user2 = User("Mandy","mandy06@gmail.com")
print(user1.username)
print(User.user_count)