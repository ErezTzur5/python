import time

class Plane:
    def __init__(self):
        self.engine_started = False
        self.fuel = 10000
    
    def start_engine(self):
        if self.fuel > 0:
            if self.engine_started == True:
                print("Engine already started.")
            else:
                self.engine_started = True
                print("Engine started.")
        else:
            print("Not enough fuel to start the engine.")
    
    def stop_engine(self):
        if self.engine_started == False:
            print("Engine is already stopped.")
        else:
            print("Stopped engine")
            
    def fly(self, distance,place):
        if self.engine_started == False:
            if not self.engine_started:
                print("Engine not started. Cannot fly.")
                return
            
            required_fuel = distance * 10
            if required_fuel > self.fuel:
                print(f"Not enough fuel to travel {distance} km.")
                return
            else:
                print("Taking off...")
                time.sleep(2)  #Simulate takeoff
            
            self.fuel -= required_fuel
            flight_time = required_fuel / 100  #Time in seconds
            print(f"Flying {distance} km to {place}. Estimated flight time: {flight_time} seconds.")
            
            time.sleep(2)
            
            print("Landing...")
            time.sleep(2)  #Simulate landing
            
            print("Landed.")
            print(f"Remaining fuel: {self.fuel} liters.")
        else:
            print("You need to start the engine before attempting to fly")

    def landing(self):
        print("Landing...")
        time.sleep(2)
        print("Landed.")
    
    def check_fuel(self):
        return self.fuel
    
    def refuel(self, amount):
        if amount <= 0:
            print("Amount should be greater than 0.")
            return
        
        if self.fuel + amount > 10000:
            print(f"Cannot refuel more than {10000 - self.fuel} liters to reach maximum capacity.")
            self.fuel = 10000
        else:
            self.fuel += amount
            print(f"Refueled {amount} liters.")
        print(f"Total fuel now: {self.fuel} liters.")


passenger_plane = Plane()

combat_plane = Plane()

business_plane = Plane() 

transport_plane = Plane()

while True:
    plane_choice = input("What plane you want to fly?(1: Passenger Plane, 2: Combat Plane, 3: Business Plane, 4: Transport Plane, 5: Exit): ")
    if plane_choice == '1':
        plane_choice = passenger_plane
        print("You Chose to fly Passenger Plane")

    elif plane_choice == '2':
        plane_choice = combat_plane
        print("You Chose to fly Combat Plane")

    elif plane_choice == '3':
        plane_choice = business_plane
        print("You Chose to fly Business Plane")

    elif plane_choice == '4':
        plane_choice = transport_plane
        print("You Chose to fly Transport Plane")
        
    elif plane_choice == '5':
        print("Exiting...")

    control = input("Enter your choice (1: Start Engine, 2: Fly, 3: Stop Engine, 4: Refuel, 5: Exit): ")

    if control == '1':
        passenger_plane.start_engine()
    elif control == '2':
        place = input("Enter place you want to fly: ")
        distance = int(input("Enter distance to fly (in km): "))
        passenger_plane.fly(distance,place)
    elif control == '3':
        passenger_plane.stop_engine()
    elif control == '4':
        amount = int(input("Enter amount of fuel to refuel: "))
        passenger_plane.refuel(amount)
    elif control == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
