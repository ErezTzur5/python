class Car:
    def _init_(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

    def isVolkswagen(self):
        return self.manufacturer == "Volkswagen"

    def isBMW(self):
        return self.manufacturer == "BMW"


my_car = Car("Volkswagen", "Golf", 2020)
if my_car.isVolkswagen():
    print("manufacterur: Volkswagen")
elif my_car.isBMW():
    print("manufacturer: BMW")
else:
    print("manufacturer: Unknown")