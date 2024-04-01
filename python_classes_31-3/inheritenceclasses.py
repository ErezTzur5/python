class Car():
    model = "Form"
    def __init__(self, manufacture, model, year):
        self.manufacture = manufacture
        self.model = model
        self.year = year
    def __str__(self) -> str:
        return f"Manufacture: {self.manufacture} Model:{self.model} Year:{self.year}"
    
class Driver():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getDriverName(self):
        return self.name

class SportsCar(Car, Driver):
    def __init__(self, manufacture, model, year, driver_name, driver_gender, driver_age):
        Car.__init__(self, manufacture, model, year)
        Driver.__init__(self, driver_name, driver_gender, driver_age)

    def isSportsCar(self):
        if self.manufacture == "Ferrari":
            return True
        return False

    def isEligibleForSportDriver(self):
         if (self.age > 25 and self.year > 2017): 
             return True 
         return False

my_sports_car = SportsCar("Ferrari", "F12", 2020, "John", "Male", 30)
print(my_sports_car.manufacture)
print(my_sports_car.model)
print(my_sports_car.year) 
print(my_sports_car.isSportsCar())
print(my_sports_car.isEligibleForSportDriver())
