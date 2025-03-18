# Create a class car with attribute like brand and model.Then create instance of this class

"""        Attributes:
        - brand: The manufacturer of the car.
        - model: The specific model of the car.
        - color: The color of the car.
        - price: The price of the car in dollars.
        - top_speed: The maximum speed of the car in km/h.
        """
class Car:
    def __init__(self, brand, model, color, price, top_speed):
        
        self.brand = brand  
        self.model = model 
        self.color = color  
        self.price = price  
        self.top_speed = top_speed
                
    def start(self):
        print(f"{self.brand} {self.model} is starting with a key... ")

    def stop(self):
        print(f"{self.brand} {self.model} has stopped.⛔")

    def print_info(self):
        print(f"Car Details: \n{self.brand} {self.model}, Color: {self.color}, Price: ${self.price} Top Speed: {self.top_speed} km/h\n")

# Create an object of the Car class
my_car = Car("Toyota", "Corolla", "Red", 20000,'300km/h')

# Call the methods
my_car.print_info()  
my_car.start()       
my_car.stop()        

