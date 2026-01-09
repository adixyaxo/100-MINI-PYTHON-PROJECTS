import pandas
import time
import datetime
import openpyxl
class account:
    def __init__(self,name,account_no,balance,loan,):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        self.loan = loan
        self.account_info =  {'NAME' : self.name,'ACCOUNT NO' : self.account_no,'BALANCE' : self.balance,'LOAN' : self.loan}
    
    def save_info(self):
        df = pandas.DataFrame(self.account_info,index=[0])
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
    print("""
    ________________________________________________
    |                                              |
    |          $$$  IRON BANK SYSTEM  $$$          |
    |______________________________________________|
    |                                              |
    |   1. Create Account      2. Login            |
    |   3. Deposit             4. Withdraw         |
    |   5. Check Balance       6. Transaction Log  |
    |   7. Exit                                    |
    |______________________________________________|
    """)

    user_choice = input("ENTER YOUR CHOICE :: ")
    try:
        user_choice_int = int(user_choice)
    except Exception as e:
        pass
    
    user_choice = user_choice.strip()
    
    if user_choice.lower() == 'create account':
        user_choice_int = 1
    elif user_choice.lower() == 'login':
        user_choice_int = 2
    elif user_choice.lower() == 'deposit':
        user_choice_int = 3
    elif user_choice.lower() == 'withdraw':
        user_choice_int = 4
    elif user_choice.lower() == 'check balance' or user_choice.lower() == 'checkbalance':
        user_choice_int = 5
    elif user_choice.lower() == 'transaction log' or user_choice.lower() == 'transactionlog':
        user_choice_int = 6
    elif user_choice.lower() == 'exit':
        user_choice_int = 7
    
    if user_choice_int !=1 and user_choice_int !=2 and user_choice_int !=3 and user_choice_int !=4 and user_choice_int !=5 and user_choice_int !=6 and user_choice_int !=7:
        print("PLEASE ONLY ENTER FROM ABOVE CHOICES")
    
    
    
if __name__ == '__main__':
    main()