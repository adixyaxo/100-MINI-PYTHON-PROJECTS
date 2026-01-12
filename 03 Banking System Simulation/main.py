import pandas
import time
import datetime
import openpyxl
import random
class account:
    def __init__(self,name,account_no,balance,loan,):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        self.loan = loan
        self.account_info =  {'NAME' : self.name,'ACCOUNT NO' : self.account_no,'BALANCE' : self.balance,'LOAN' : self.loan}
    
    def save_info(self):
        df = pandas.DataFrame(self.account_info,index=[0])
        df.to_excel(f"03 Banking System Simulation/accounts/{self.account_no}.xlsx",index=False)

    def getinfo(self):
        print(f"NAME :: {self.name}\nBALANCE :: {self.balance}\nLOAN :: {self.loan}")

class savings_account(account):
    def __init__(self,name,account_no,balance,loan,intrest):
        super().__init__(name,account_no,balance,loan)
        self.intrest = intrest
        self.account_info["Account Type"] = "Savings Account"
        
    def getinfo_(self):
        self.getinfo()
        print(f"\nINTREST :: {self.intrest}")
    
    def save_info(self):
        df = pandas.DataFrame(self.account_info,index=[0])
        df.to_excel(f"03 Banking System Simulation/accounts/{self.account_no}.xlsx",index=False)
        
class current_account(account):
    def __init__(self,name,account_no,balance,loan,intrest):
        super().__init__(name,account_no,balance,loan)
        self.intrest = intrest
        self.account_info["Account Type"] = "Current Account"
        
    def getinfo_(self):
        self.getinfo()
        print(f"\nINTREST :: {self.intrest}")
        
    def save_info(self):
        df = pandas.DataFrame(self.account_info,index=[0])
        df.to_excel(f"03 Banking System Simulation/accounts/{self.account_no}.xlsx",index=False)
        
aditya = savings_account("aditya",727,10000,10,21)
aditya.getinfo()
    
def random_acc_no():
    accountno = random.randint(1,1000000)
    for item in accountsnos:
        if accountno == item:
            return random_acc_no()
        else:
            return accountno
    
accountnos = (pandas.read_excel("accounts.xlsx"))
accountnos = tuple(accountnos[0])

def create_account():
    name = input("Please Enter Your Name  ::  ")
    amount = input("Enter the amount you want to deposit in your account  ::  ")
    loan = 0
    type = input("Enter what type of account do you want to create\n1. Savings Account\n2. Current Account\nYOUR CHOICE  ::  ")
    
    if type=='1' or type.strip().lower() == 'savings account' or type.strip().lower() == 'savingsaccount' or type.strip().lower() == 'saving account' or type.strip().lower() == 'savingaccount' or type.strip().lower() == 'savings' or type.strip().lower() == 'saving':
        saving_intrest = 10
        accountno = random_acc_no()
        print(f"Your generated account no is {accountno}")
        accountnos.add(accountno)
        save_account_nos()

        
def save_account_nos():
    accountno_df = pandas.DataFrame(accountnos)
    accountno_df.to_excel(f"03 Banking System Simulation/accounts.xlsx",index=False)

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
    
    if user_choice_int == 1:
        create_account()
    
if __name__ == '__main__':
    main()