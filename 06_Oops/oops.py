class Car:
    
    total_car = 0 

    def __init__(self, brand, model):
        self.__model = model
        self.__brand = brand
        Car.total_car += 1
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):  
        return self.__brand
    
    def fuel_type(self):  
        return "Petrol / Diesel"
    
    @staticmethod
    def general_description():  
        return "A car is meant for transport."
    
    @property
    def get_model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  
        self.battery_size = battery_size  
    
    def fuel_type(self):  
        return "Electric Charge"


# Creating objects
my_new_car = Car("Toyota", "Corolla")  
my_electric_car = ElectricCar("Tesla", "Model S", "10kWh")  

# Correct way to call a static method
print(Car.general_description())  # ✅ Best practice

# It also works with objects (but not recommended)
print(my_new_car.general_description())  # ⚠️ Works but not ideal
print(my_electric_car.general_description())  # ⚠️ Works but not ideal

print(my_new_car.get_model)
print(isinstance(my_electric_car,Car))
print(isinstance(my_electric_car,ElectricCar))    

class Battery :
    def battery_info(self):
        return "This is battery"

class Engine :
    def engine_info(self):
        return "this is Engine"
    
class ElectricCarTwo(Battery, Engine ,Car):
    pass

my_tesla = ElectricCarTwo("Tesla" , "Model-S")

print(my_tesla.battery_info())
print(my_tesla.engine_info())