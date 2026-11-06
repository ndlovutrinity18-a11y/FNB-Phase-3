#Encapsulation 
#is a fundamental principle of OOP that involves bundling the data,attributes, fields 
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute to store the account balance
        
        
    @property
    def balance (self):
       return self.__balance 
   
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value  
    
    def deposit (self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        
    def withdraw(self, amount):
        if amount <=0:
            raise ValueError("Withdrawal must be positive")
        if amount >= self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        
account = BankAccount()
account.deposit(100)
account.withdraw(50)
print(account.balance)

