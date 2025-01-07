class Car:
    def __init__(self, model, year):
        #Theese are attributes
        self.model = model
        self.year = year
    
    def __str__(self):
        return f"Car: {self.model} {self.year}"

    def custom_method(self):
        return f"Car: {self.model} {self.year}"



if __name__ == "__main__":
    car = Car("Toyota", 2020)
    print(car)
    print(car.custom_method())
        