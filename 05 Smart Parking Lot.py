#   - [ ] 05. Smart Parking Lot
    
#       - Classes: Vehicle (plate, type), Ticket (timestamp), ParkingLot.
#       - Features: Calculate fee based on time, manage spot availability.

import time

#  The cost of the ticket would be calculated on the based of the entry and exit time of the vechicle also taking in consideration the type of vehicle.

class vehicle:
    def __init__(self, plate, type, color, model, owner_name):
        self.plate = plate
        self.type = type #this will register the type of vehicle eg car, bike, truck
        self.color = color
        self.model = model
        self.owner_name = owner_name
        self.entry_time = time.time()

class ticket: