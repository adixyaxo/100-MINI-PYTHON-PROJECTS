from turtle import pd
import pandas
import time
import datetime
import openpyxl
import random
class account:
    def __init__(self,name,account_no,balance,loan,pin):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        self.loan = loan
        self.pin = pin
        self.type = None
        self.account_info =  {'NAME' : self.name,'ACCOUNT NO' : self.account_no,'BALANCE' : self.balance,'LOAN' : self.loan, 'PIN' : self.pin , 'CREATED AT' : datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), }

    def getinfo(self):
        print(f"NAME :: {self.name}\nBALANCE :: {self.balance}\nLOAN :: {self.loan}")

class savings_account(account):
    def __init__(self,name,account_no,balance,loan,intrest,pin):
        super().__init__(name,account_no,balance,loan,pin)
        self.intrest = intrest
        self.account_info["Account Type"] = "Savings Account"
        
    def getinfo_(self):
        self.getinfo()
        print(f"\nINTREST :: {self.intrest}")
    
    def save_info(self):
        df = pandas.DataFrame(self.account_info,index=[0])
        df.to_excel(f"accounts/saving/{self.account_no}.xlsx",index=False)
        
class current_account(account):
    def __init__(self,name,account_no,balance,loan,intrest,pin):
        super().__init__(name,account_no,balance,loan,pin)
        self.intrest = intrest
        self.account_info["Account Type"] = "Current Account"
        
    def getinfo_(self):
        self.getinfo()
        print(f"\nINTREST :: {self.intrest}")
        
    def save_info(self):
        df = pandas.DataFrame(self.account_info,index=[0])
        df.to_excel(f"accounts/current/{self.account_no}.xlsx",index=False)
        
accountnos = (pandas.read_excel("accounts_list.xlsx"))
accountnos = set(accountnos[0])

def random_acc_no():
    accountno = random.randint(1,1000000)
    for item in accountnos:
        if accountno == item:
            return random_acc_no()
        else:
            return accountno
    

def create_account():
    name = input("Please Enter Your Name  ::  ")
    amount = input("Enter the amount you want to deposit in your account  ::  ")
    loan = 0
    type = input("Enter what type of account do you want to create\n1. Savings Account\n2. Current Account\nYOUR CHOICE  ::  ")
    pin = input("Set a 4 digit pin for your account  ::  ")
    
    
    if type=='1' or type.strip().lower() == 'savings account' or type.strip().lower() == 'savingsaccount' or type.strip().lower() == 'saving account' or type.strip().lower() == 'savingaccount' or type.strip().lower() == 'savings' or type.strip().lower() == 'saving':
        saving_intrest = 10
        accountno = random_acc_no()
        print(f"Your generated account no is {accountno}")
        accountnos.add(accountno)
        save_account_nos()
        account = savings_account(name,accountno,amount,loan,saving_intrest,pin)
        account.save_info()
        
    elif type=='2' or type.strip().lower() == 'current account' or type.strip().lower() == 'currentaccount' or type.strip().lower() == 'currents account' or type.strip().lower() == 'currentsaccount' or type.strip().lower() == 'currents' or type.strip().lower() == 'current':
        current_intrest = 0
        accountno = random_acc_no()
        print(f"Your generated account no is {accountno}")
        accountnos.add(accountno)
        save_account_nos()
        account = current_account(name,accountno,amount,loan,current_intrest,pin)
        account.save_info()
    else:
        print("WRONG CHOICE TRY AGAIN LATER")
        
def login():
    user_name = input("ENTER YOUR NAME  ::  ")
    user_name = user_name.strip().lower().capitalize()
    global user_account_no_global
    try :
        user_account_no_global = input("ENTER YOUR ACCOUNT NO  ::  ")
        user_account_no_global = int((user_account_no_global.strip()).lower())
    except Exception as e:
        print(e)
    user_pin = input("ENTER YOUR 4 DIGIT PIN  ::  ")
    user_pin = int(user_pin.strip().lower())
    type = input("ENTER YOUR ACCOUNT TYPE\n1. Savings Account\n2. Current Account\nYOUR CHOICE  ::  ")
    global user_path
    if type=='1' or type.strip().lower() == 'savings account' or type.strip().lower() == 'savingsaccount' or type.strip().lower() == 'saving account' or type.strip().lower() == 'savingaccount' or type.strip().lower() == 'savings' or type.strip().lower() == 'saving':
        user_path = f"accounts/saving/{user_account_no_global}.xlsx"
    elif type=='2' or type.strip().lower() == 'current account' or type.strip().lower() == 'currentaccount' or type.strip().lower() == 'currents account' or type.strip().lower() == 'currentsaccount' or type.strip().lower() == 'currents' or type.strip().lower() == 'current':
        user_path = f"accounts/current/{user_account_no_global}.xlsx"
    try:
        account_file = pandas.read_excel(user_path)
        account_name = account_file['NAME'][0]
        account_name = account_name.strip().lower().capitalize()
        account_pin = account_file['PIN'][0]
        if user_name == account_name and user_pin == int(account_pin):
            return "LOGIN SUCCESSFUL"
        else:
            return "LOGIN FAILED PLEASE CHECK YOUR CREDENTIALS"
    except Exception as e:
        return None
        print(e)
        print("ACCOUNT NOT FOUND PLEASE CHECK YOUR ACCOUNT NO")
    
def deposit():
    if login() == "LOGIN SUCCESSFUL":
        deposit_amount = input("ENTER THE AMOUNT YOU WANT TO DEPOSIT  ::  ")
        account_file = pandas.read_excel(user_path)
        account_balance = account_file['BALANCE'][0]
        account_balance = int(account_balance) + int(deposit_amount)
        account_file['BALANCE'][0] = account_balance
        transaction = f"DEPOSITED {deposit_amount} TO ACCOUNT {user_account_no_global} ON {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
        new_column_name = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        account_file[new_column_name] = pd.NA
        account_file[new_column_name][0] = transaction
        account_file.to_excel(user_path,index=False)
        print(f"YOU HAVE SUCCESSFULLY DEPOSITED {deposit_amount} TO YOUR ACCOUNT :: {user_account_no_global}\nYOUR NEW BALANCE IS :: {account_balance}")
        

        
        
def withdraw():
    if login() == "LOGIN SUCCESSFUL":
        withdraw_amount = input("ENTER THE AMOUNT YOU WANT TO WITHDRAW  ::  ")
        account_file = pandas.read_excel(user_path)
        account_balance = account_file['BALANCE'][0]
        account_balance = int(account_balance) - int(withdraw_amount)
        transaction = f"WITHDRAWN {withdraw_amount} FROM ACCOUNT {user_account_no_global} ON {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
        new_column_name = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        account_file[new_column_name] = pd.NA
        account_file[new_column_name][0] = transaction
        account_file['BALANCE'][0] = account_balance
        account_file.to_excel(user_path,index=False)
        print(f"YOU HAVE SUCCESSFULLY WITHDRAWN {withdraw_amount} FROM YOUR ACCOUNT :: {user_account_no_global}\nYOUR NEW BALANCE IS :: {account_balance}")
        

def check_balance():
    if login() == "LOGIN SUCCESSFUL":
        account_file = pandas.read_excel(user_path)
        account_balance = account_file['BALANCE'][0]
        print(f"YOUR CURRENT BALANCE IS :: {account_balance}")

def transaction_log():
    if login() == "LOGIN SUCCESSFUL":
        account_file = pandas.read_excel(user_path)
        print("YOUR TRANSACTION LOG IS AS FOLLOWS :: ")
        for col in account_file.columns:
            if col not in ['NAME','ACCOUNT NO','BALANCE','LOAN','PIN','Account Type','CREATED AT']:
                print(account_file[col][0])

def save_account_nos():
    accountno_df = pandas.DataFrame(accountnos)
    accountno_df.to_excel(f"accounts.xlsx",index=False)

def main():
    while True:
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
        
        if user_choice.lower() == 'create account' or user_choice.lower() == 'createaccount':
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
        elif user_choice_int == 2:
            print(login())
        elif user_choice_int == 3:
            deposit()
        elif user_choice_int == 4:
            withdraw()
        elif user_choice_int == 5:
            check_balance()
        elif user_choice_int == 6:
            transaction_log()
        elif user_choice_int == 7:
            print("THANK YOU FOR USING IRON BANK SYSTEM")
            time.sleep(2)
            exit()
    
if __name__ == '__main__':
    main()