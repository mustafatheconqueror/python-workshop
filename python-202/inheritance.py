class Animal:
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self) # This is how we call the parent class constructor
        print("Dog created")

    def who_am_i(self):
        # Override
        print("I am a dog")

if __name__ == "__main__":
    animal = Animal()
    dog = Dog()
    dog.who_am_i()