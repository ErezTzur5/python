import time

class Plane:
    def __init__(self, plane_type, fuel_consumption_rate):
        self.engine_started = False
        self.fuel = 10000
        self.plane_type = plane_type
        self.fuel_consumption_rate = fuel_consumption_rate
    
    def start_engine(self):
        if self.fuel > 0:
            if self.engine_started:
                print(f"{self.plane_type} Engine already started.")
            else:
                self.engine_started = True
                print(f"{self.plane_type} Engine started.")
        else:
            print(f"{self.plane_type} Not enough fuel to start the engine.")
    
    def stop_engine(self):
        if not self.engine_started:
            print(f"{self.plane_type} Engine is already stopped.")
        else:
            self.engine_started = False
            print(f"{self.plane_type} Stopped engine")
            
    def fly(self, distance, place):
        if not self.engine_started:
            print(f"{self.plane_type} Engine not started. Cannot fly.")
            return
        
        required_fuel = distance * self.fuel_consumption_rate
        if required_fuel > self.fuel:
            print(f"{self.plane_type} Not enough fuel to travel {distance} km.")
            return
        
        print(f"{self.plane_type} Taking off...")
        time.sleep(2)  #Simulate takeoff
        
        self.fuel -= required_fuel
        flight_time = required_fuel / 100  # Time in seconds
        print(f"{self.plane_type} Flying {distance} km to {place}. Estimated flight time: {flight_time} seconds.")
        
        time.sleep(2)
        
        print(f"{self.plane_type} Landing...")
        time.sleep(2)  #Simulate landing
        
        print(f"{self.plane_type} Landed.")
        print(f"{self.plane_type} Remaining fuel: {self.fuel} liters.")
    
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
            print(f"{self.plane_type} Refueled {amount} liters.")
        
        print(f"{self.plane_type} Total fuel now: {self.fuel} liters.")


passenger_plane = Plane("Passenger Plane", 10)  # 10 liters per km

combat_plane = Plane("Combat Plane", 50)  # 50 liters per km

business_plane = Plane("Business Plane", 15)  # 15 liters per km

transport_plane = Plane("Transport Plane", 20)  # 20 liters per km

while True:
    print("\nChoose a plane to operate:")
    print("1. Passenger Plane")
    print("2. Combat Plane")
    print("3. Business Plane")
    print("4. Transport Plane")
    print("5. Exit")
    
    plane_choice = input("Enter your choice: ")
    
    if plane_choice == '1':
        plane = passenger_plane
        print("You Chose to fly Passenger Plane")

    elif plane_choice == '2':
        plane = combat_plane
        print("You Chose to fly Combat Plane")

    elif plane_choice == '3':
        plane = business_plane
        print("You Chose to fly Business Plane")

    elif plane_choice == '4':
        plane = transport_plane
        print("You Chose to fly Transport Plane")
        
    elif plane_choice == '5':
        print("Exiting...")
        break

    while True:
        control = input("Enter your choice (1: Start Engine, 2: Fly, 3: Stop Engine, 4: Refuel, 5: Exit): ")

        if control == '1':
            plane.start_engine()
        elif control == '2':
            place = input("Enter place you want to fly: ")
            distance = int(input("Enter distance to fly (in km): "))
            plane.fly(distance, place)
        elif control == '3':
            plane.stop_engine()
        elif control == '4':
            amount = int(input("Enter amount of fuel to refuel: "))
            plane.refuel(amount)
        elif control == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
