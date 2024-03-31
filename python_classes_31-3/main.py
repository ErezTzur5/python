# class Car:
#     def __init__(self, manufacturer, name=''):
#         self.manufacturer = manufacturer
#         self.name = name
#         self. email = f'{name}@company.com'
#     def __str__(self) :
#         return f''
    
    
# my_car1 = Car ('bmw')
# print (my_car1. name)
# print (my_car1.manufacturer)
# print (my_car1. email)


class Person:
    def __init__(self,name,age,eye_color) -> None:
        self.name = name
        self.age = age
        self.eye_color = eye_color
    def __str__(self) -> str:
        return f"Name:{self.name},Age:{self.age} Eyes color:{self.eye_color}"
    
erez = Person(name='Erez',age='24.4',eye_color='Brown')
tal = Person(name='Tal',age='24',eye_color='Black')
print(f"Erez:\n{erez}\nTal:\n{tal}")

class Plane:
    def __init__(self,company_name,plane_color,capacity) -> None:
        self.company_name = company_name
        self.plane_color = plane_color
        self.capacity = capacity
        
    def __str__(self) -> str:
        return f"Company name:{self.company_name},Plane color:{self.plane_color} Capacity:{self.capacity}"
    
el_al = Plane(company_name="EL AL",plane_color="White",capacity=100)
arkia = Plane(company_name="ARKIA",plane_color="RED",capacity=120)
print(el_al)
print(arkia)

class Door:
    def __init__(self,door_color,door_price,door_type) -> None:
        self.door_color = door_color
        self.door_price = door_price
        self.door_type = door_type
        
    def __str__(self) -> str:
        return f"Door color:{self.door_color},Door Price:{self.door_price} Door Type:{self.door_type}"
            
door1 = Door(door_color="Brown",door_price="20$",door_type="Wood")
door2 = Door(door_color="Black",door_price="80$",door_type="Metal")
print(door1)
print(door2)

class Furniture:
    def __init__(self,type_of_furniture,color_of_furniture,price) -> None:
        self.type_of_furniture = type_of_furniture
        self.color_of_furniture = color_of_furniture
        self.price = price
        
    def __str__(self) -> str:

        return f"Type:{self.type_of_furniture},Color:{self.color_of_furniture} Price:{self.price}"

chair = Furniture(type_of_furniture="Chair",color_of_furniture="White",price="50$")
table = Furniture(type_of_furniture="Table",color_of_furniture="White",price="150$")
print(chair)
print(table)