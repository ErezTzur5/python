import time

class Plane:
    def __init__(self,plane_type="", capacity="", max_speed="",plane_color="",engine="",wingspan="",weight="",flight_range ="",flight_attendants="",fuel_range=1000,destination = '',destination_km=0) -> None:
        self.is_on = False
        self.plane_type = plane_type
        self.capacity = capacity
        self.max_speed = max_speed
        self.plane_color = plane_color
        self.engine = engine
        self.wingspan = wingspan
        self.weight = weight
        self.flight_range = flight_range
        self.flight_attendants = flight_attendants
        self.fuel = True
        self.feul_range = fuel_range
        self.wheels = True
        self.destination = destination
        self.destination_km = destination_km

    def __str__(self) -> str:
        return f"Plane Type: {self.plane_type}\nCapacity: {self.capacity}\nMax Speed: {self.max_speed}\nPlane Color: {self.plane_color}\nEngine: {self.engine}\nWingspan: {self.wingspan}\nWeight: {self.weight}\nFlight Range: {self.flight_range}\nFlight Attendants: {self.flight_attendants}"

    def fly(self): #flying func
        if self.is_on and self.fuel is True:
            if self.destination > self.flight_range:
                print("Cant put destination that is far from the range flight")
            else:
                self.flight_range = self.flight_range - self.destination
                print("Flying!")
                time.sleep(1)
                print(f"Flight range that remains are {self.flight_range}")
        else:
            print("Engine is off")

    def start_engine(self): #starting engine
        if self.is_on == False:
            if self.fuel == True: 
                self.is_on = True
                print(f"{self.plane_type},started the engine")
            else:
                print(f"{self.plane_type}, have low fuel! Cant start engine")
        else:
            print(f"{self.plane_type},already on!.")
    
    def takeoff(self): #start flying
        if self.is_on == False:
            print("need to start the engine first!")
            return False
        else:
            print("Taking off!")
            self.wheels = False
            time.sleep(1)
            print("Took Off,losing wheels!")
            return True
        

    def landing(self):#landing
        if self.wheels == False:
            self.wheels = True
            print("Opening wheels for landing!...")
            time.sleep(1)
            print("Landing..")
            time.sleep(1)
            print("Closing wheels after land!")
            self.wheels = False

        else:
            print("Wheels already opened")

    def stop_engine(self): #stopping engine
        if self.is_on == True:
            self.is_on = False
            print(f"{self.plane_type},stopped the engine")
        else:
            print(f"{self.plane_type},engine is already off!.")

    def refuel(self): #refueller
        if self.fuel == True:
            if self.is_on is not False:
                print(f"{self.plane_type} No need to refueling yet.")
            else:
                print(f"Please stop engine before refueling")
        else:    
            print(f"Refueling {self.plane_type}")

#Normal Plane
normal_plane = Plane("Boeing 747", 416, 988, "White", "Jet", 68.4, 439985, 9800, 15)

def main():
    while True:
        plane = input("""Please choose a plane you want to fly with  or [C]lose (1-4)
1.#Normal Plane
2.#Military Plane
3.#BigAir Plane
4.#Plane                
""").lower()
        if plane == '1':
            normal_plane = Plane("Boeing 747", 416, 988, "White", "Jet", 68.4, 439985, 9800, 15)
        if plane == 'c':
            print('stopping program')
            break

        start = input("""Start engine? Y/N or [C](to stop program)""").lower()
        if start == 'y':
            normal_plane.start_engine()
        elif start == 'n':
            print('You need to start the engine if you want to start flying')
        else:
            print("User Chose to not start engine")
        
        destination = int(input("""Place the number of km you want to fly\n"""))
        if destination > 0 :
            take_off = normal_plane.takeoff()
            if take_off is True:
                normal_plane.destination = destination
                fly = normal_plane.fly()





        

if __name__ == "__main__":
    main()
