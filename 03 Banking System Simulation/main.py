import pandas as pd
import openpyxl
class account:
    def __init__(self,name,account_no,balance,loan,):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        self.loan = loan
        self.account_info =  {'NAME' : self.name,'ACCOUNT NO' : self.account_no,'BALANCE' : self.balance,'LOAN' : self.loan}
    
    def save_info(self):
        df = pd.DataFrame(self.account_info,index=[0])
        df.to_excel(f"03 Banking System Simulation/{self.account_no}.xlsx",index=False)

    def getinfo(self):
        print(f"NAME :: {self.name}\nBALANCE :: {self.balance}\nLOAN :: {self.loan}")

class savings_account(account):
    def __init__(self,name,account_no,balance,loan,intrest):
        super().__init__(name,account_no,balance,loan)
        self.intrest = intrest
        
    def getinfo_(self):
        self.getinfo()
        print(f"\nINTREST :: {self.intrest}")
        
class current_account(account):
    def __init__(self,name,account_no,balance,loan,intrest):
        super().__init__(name,account_no,balance,loan)
        self.intrest = intrest
    
    def getinfo_(self):
        self.getinfo()
        print(f"\nINTREST :: {self.intrest}")
        
aditya = savings_account("aditya",727,10000,10,21)
aditya.getinfo()

def main():
    print(aditya.account_info)
    aditya.save_info()

if __name__ == '__main__':
    main()