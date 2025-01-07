def string_slicing():
    my_string = "Hello World"
    print(my_string[0:5]) # prints Hello
    print(my_string[3:6]) # prints lo W
    print(my_string[6:]) # prints World
    print(my_string[0:5:2]) # prints Hlo
    print(my_string[::-1]) 
    print(my_string[::1]) # prints HloWrd


def string_methods():
    my_string2 = "deneme"
    print(my_string2.capitalize())



def print_formatting():
    name = "John"
    age = 30
    print(f"My name is {name} and I am {age} years old")


if __name__ == "__main__":
    #string_slicing()
    #string_methods()
    print_formatting()

