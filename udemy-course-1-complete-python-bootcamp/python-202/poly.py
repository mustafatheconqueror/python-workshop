class Animal:
    amIdAnimal = True
    def __init__(self, name):
        self.name = name
        print("Animal created")

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return self.name + " says woof"
    
class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
    
    def speak(self):
        return self.name + " says meow"

def pet_speak(pet):
    print(pet.speak())

if __name__ == "__main__":
    dog = Dog("Dog")
    cat = Cat("Cat")

    animals = [dog, cat]
    for animal in animals:
        pet_speak(animal)

    