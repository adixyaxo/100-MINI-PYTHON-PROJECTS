class account:
    def __init__(self,name,account_no,balance,loan,):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        self.loan = loan

    def getinfo(self):
        print(f"NAME :: {self.name}\nBALANCE :: {self.balance}\nLOAN :: {self.loan}")

class savings_account(account):
    def __init__(self,name,account_no,balance,loan,intrest):
        super().__init__(name,balance,loan)
        self.intrest = intrest
        
    def getinfo_(self):
        self.getinfo()
        print(f"\nINTREST :: {self.intrest}")
        
class current_account(account):
    def __init__(self,intrest):
        self.intrest = intrest
    
    def getinfo_(self):
        self.getinfo()
        print(f"\nINTREST :: {self.intrest}")
        
aditya = savings_account("aditya")
aditya.getinfo()