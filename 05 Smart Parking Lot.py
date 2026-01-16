#   - [ ] 05. Smart Parking Lot
    
#       - Classes: Vehicle (plate, type), Ticket (timestamp), ParkingLot.
#       - Features: Calculate fee based on time, manage spot availability.

import time
import random
import pandas as pd
import openpyxl


fee_per_second = 1
#  The cost of the ticket would be calculated on the based of the entry and exit time of the vechicle also taking in consideration the type of vehicle.

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
        df = {"PLATE" : self.plate , "type" : self.type, "color"}
        


def entry():
    plate = input("Enter your plate no : ")
    type = input("Enter your vehicle type : ")
    color = input("Enter your vehicle color : ")
    model = input("Enter your vehicle model : ")
    owner_name = input("Enter your name : ")
    print(f"Vehicle {plate} has been parked at {time.time()} by {owner_name}")
    return vehicle(plate, type, color, model, owner_name)

def exit():
    plate = input("Enter your plate no : ")
    ticket_id_user = input("Enter your ticket id : ")
    
    return vehicle.exit_time

def calculate_fee(entry_time, exit_time):
    fee = (exit_time - entry_time) * fee_per_second
    