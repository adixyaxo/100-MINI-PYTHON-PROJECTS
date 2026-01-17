#   - [ ] 05. Smart Parking Lot
    
#       - Classes: Vehicle (plate, type), Ticket (timestamp), ParkingLot.
#       - Features: Calculate fee based on time, manage spot availability.

import time
import random
import pandas as pd
import openpyxl

file_path = "parking_lot.xlsx"
fee_per_second = 1
max_parking_slots = 1000
#  The cost of the ticket would be calculated on the based of the entry and exit time of the vechicle also taking in consideration the type of vehicle.



start_sheet_row_max = 0
def loading_workbook():
    book = openpyxl.load_workbook("parking_lot.xlsx")
    global start_sheet_row_max
    sheet = book.active
    start_sheet_row_max = sheet.max_row
    
def check_limit():
    if start_sheet_row_max >= max_parking_slots:
        return 1
    else:
        return 0

class vehicle:
    def __init__(self, plate, type, color, model, owner_name):
        self.plate = plate
        self.type = type #this will register the type of vehicle eg car, bike, truck
        self.color = color
        self.model = model
        self.owner_name = owner_name
        self.entry_time = time.time()
        self.ticket_id = f"{self.plate}-{random.randint(1000,9999)}"
        self.exit_time = None
    
    def save_info_excel(self):
        _dict = {"PLATE" : self.plate , "type" : self.type, "color" : self.color, "model" : self.model, "owner" : self.owner_name, "entry_time" : self.entry_time, "ticket_id" : self.ticket_id}
        df = pd.DataFrame(_dict , index=[0])
        try:
            with pd.ExcelWriter(file_path,engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                global start_sheet_row_max
                df.to_excel(writer,index=False,header=False,startrow=start_sheet_row_max)
                start_sheet_row_max = start_sheet_row_max + 1
        except Exception as e:
            return e
   
def test():
    test_car = vehicle("1234567890", "car", "red", "Toyota", "John Doe")
    test_car.save_info_excel()
    test_car_2 = vehicle("test car", "car", "red", "Toyota", "John Doe")
    test_car_2.save_info_excel()


def check_for_car():
    plate = input("Enter the vehicle plate no : ")
    df = pd.read_excel("parking_lot.xlsx")
    if plate in df['PLATE'].values:
        row = df[df['PLATE'] == plate]
        print("Vehicle found in the parking lot")
        return row
    else:
        print("Vehicle not found in the parking lot")
        return 0

def verify():
    ticket_id = input("Enter the ticket id : ")
    vehicle_row = check_for_car()
    if vehicle_row == 0:
        return 0
    else:
        if ticket_id == vehicle_row["ticket_id"]:
            return vehicle_row
        else:
            return -1


def entry():
    plate = input("Enter the vehicle plate no : ")
    type = input("Enter the vehicle type : ")
    color = input("Enter the vehicle color : ")
    model = input("Enter the vehicle model : ")
    owner_name = input("Enter the owner name : ")
    print(f"Vehicle {plate} has been parked at {time.time()} by {owner_name}")
    return vehicle(plate, type, color, model, owner_name)

def exit_car():
    plate = input("Enter the vehicle plate no : ")
    ticket_id_user = input("Enter the ticket id : ")
    if verify() != 0 and verify() != -1:
        


def calculate_fee(entry_time, exit_time):
    fee = (exit_time - entry_time) * fee_per_second
    
    
def main():
    loading_workbook()
    test()
    while True:
        print("""
        ________________________________________________
        |                                              |
        |       $$$  SMART PARKING SYSTEM  $$$         |
        |______________________________________________|
        |                                              |
        |   1. Register New Entry                      |
        |   2. Exit a Vehicle                          |
        |   3. Check for a Car                         |
        |   4. Verify Ticket                           |
        |   5. Exit System                             |
        |______________________________________________|
        """)
        
        
        user_choice = input("ENTER YOUR CHOICE :: ")
        
        user_choice = user_choice.strip().lower()
        
        if user_choice in ["1", "register", "register new entry", "register a new entry", "registernewentry", "registeranewentry", "new"]:
            user_choice = 1
        elif user_choice in ["2", "exit", "exit vehicle", "exitvehicle", "exitavehicle", "exit a vehicle", "leave", "checkout"]:
            user_choice = 2
        elif user_choice in ["3", "check", "check for a car", "check car", "find car", "search car", "search", "find", "findcar", "checkcar", "checkforcar", "checkforacar"]:
            user_choice = 3
        elif user_choice in ["4", "verify", "verify ticket", "ticket", "check ticket","verifyticket", "checkticket"]:
            user_choice = 4
        elif user_choice in ["5", "exit system", "quit", "close", "end", "stop","exit", "leave", "logout", "sign out", "signout","exitsystem"]:
            user_choice = 5

        if user_choice == 1:
            if check_limit() == 1:
                print("THERE ARE NO MORE SLOTS AVAILABLE FOR PARKING")
                continue
            entry()
        elif user_choice == 2:
            if check_for_car() != 0 :
                exit_car()
        elif user_choice == 3:
            check_for_car()
        elif user_choice == 4:
            print("Feature not implemented yet.")
        elif user_choice == 5:    
            print("Exiting system...")
            time.sleep(2)        
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()