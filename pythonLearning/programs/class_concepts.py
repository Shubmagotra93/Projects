class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model   # make model private and no one changes its value, create separate method and mark it as property decorator
        Car.total_cars +=1

# have made brand attribute private so outside class can not access it
    # so to access brand outside the class, we need to create getter method
# This is encapsulation concept
    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.__model}"

# Polymorphism concept as same method in both Car and ElectricCar class
    def fuel_type(self):
        return "Petrol or Diesel"

# if you do not want to change value of model in any-case, use property decorator,
# but while accessing this method you only need to pass it like property/attribute no need to pass brackets
    @property
    def model(self):
        return self.__model

# static methods not needs self in method args and are called directly by class name
    @staticmethod
    def general_description():
        return "Cars are means of transport"


class ElectricCar(Car):

    def __init__(self,brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"



my_car = Car("Tata", "Nexon")
# print(my_car.__brand)
# print(my_car.model)
# print(my_car.full_name())
# print(my_car.fuel_type())
# my_car.model = "Punch"
# print(my_car.model)  # this is model method not model attribute but as it is property decorated,
# so no need to use brackets while calling this method
print(isinstance(my_car, Car))  # True
print(isinstance(my_car, ElectricCar))  # False my_car is instance of Car class not ElectricCar


# safari = Car("Tata", "TOP MODEL")
# swift = Car("Maruti", "Swift")
# print(swift.general_description())
# # print(Car.general_description())

# print(Car.total_cars)



my_Electric_car = ElectricCar("Tesla", "Model S", "85Kwh")
# print(my_Electric_car.model)
# print(my_Electric_car.full_name())
# print(my_Electric_car.__brand)  # cannot access outside the class
# print(my_Electric_car.get_brand()) # can access brand through getter method
# print(my_Electric_car.fuel_type())
# my_Electric_car.model = "Mclearn"  # AttributeError: property 'model' of 'ElectricCar' object has no setter
# print(my_Electric_car.model)
print(isinstance(my_Electric_car, ElectricCar))


