class Car:
    
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model  

    # Method
    def car_details(self):
        return f"Car: {self.brand}, Model: {self.model}"

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla")
print(my_car.car_details())  