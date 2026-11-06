class BankAcount:
    MIN_BALANCE = 100
    
    def __init__(self,owner, balance =0):
        self.owner = owner
        self._balance = balance
        
    def deposit (self, amount):
        if amount >0:
            self._balance += amount
            print(f"{self.owner}'s new balace: R{self._balance}")
        else:
            print("Deposit Amount must be positive")
            
            
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<= rate <=5
    
account = BankAcount("Mandy",250)
account.deposit(100)

print(BankAcount.is_valid_interest_rate(4))
print(BankAcount.is_valid_interest_rate(10))