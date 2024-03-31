import time

class Plane:
    def __init__(self):
        self.engine_started = False
        self.fuel = 10000
    
    def start_engine(self):
        if self.fuel > 0:
            self.engine_started = True
            print("Engine started.")
        else:
            print("Not enough fuel to start the engine.")
    
    def stop_engine(self):
        self.engine_started = False
        print("Engine stopped.")
    
    
    def fly(self, distance):
        if not self.engine_started:
            print("Engine not started. Cannot fly.")
            return
        
        required_fuel = distance * 10
        if required_fuel > self.fuel:
            print(f"Not enough fuel to travel {distance} km.")
            return
        
        print("Taking off...")
        time.sleep(2)  # Simulate takeoff
        
        self.fuel -= required_fuel
        flight_time = required_fuel / 100  # Time in seconds
        print(f"Flying {distance} km. Estimated flight time: {flight_time} seconds.")
        
        # time.sleep(flight_time)  # Simulate flight
        time.sleep(2)
        
        print("Landing...")
        time.sleep(2)  # Simulate landing
        
        print("Landed.")
        print(f"Remaining fuel: {self.fuel} liters.")
    
    def landing(self):
        print("Landing...")
        time.sleep(2)  # Simulate landing
        print("Landed.")
    
    def check_fuel(self):
        return self.fuel

# Example usage
plane = Plane()

plane.start_engine()
plane.fly(500)
# print(f"Remaining fuel: {plane.check_fuel()} liters.")
plane.landing()
plane.stop_engine()
