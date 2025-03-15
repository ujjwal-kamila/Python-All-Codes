# Create a class car with attribute like brand and model.Then create instance of this class

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model



# create a object
my_car = Car("Toyota","corolla")
print(my_car.brand)
print(my_car.model)
