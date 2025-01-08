
def for_in_loop():
    numbers = [1, 2, 3, 4, 5]
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is even number") 
        else:
            print(f"{number} is odd number")


def print_dictionary():
    my_dict = {"name": "Mustafa", "age": 25,}
    for key, value in my_dict.items():
        print(f"key: {key} value: {value}")



def while_loop_examle():
    i = 0
    while i < 10:
        print(i)
        i += 1

def break_and_continue():
    for i in range(1, 10):
        if i == 5:
            break
        print(i)

def write_only_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for number in numbers:
        if number % 2 == 0:
            print(number)
        else:
            continue

def learn_pass_statement():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for number in numbers:
        if number == 4:
            pass
        else:
            print(number)

def use_range_function():
    for i in range(1, 10):
        print(i)

def use_range_function_with_step():
    for i in range(1, 10, 2):
        print(i)

def use_enumerate_function():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for index, number in enumerate(numbers): # enumerate return list of tuple
        print(f"index: {index} number: {number}")

def use_zip_function():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    for number, letter in zip(numbers, letters):
        print(f"number: {number} letter: {letter}")


def use_in_function():
    number = 3
    if number in [1,2,3]:
        print("number is in the list")
    else:
        print("number is not in the list")

def use_input():
    name = input("Enter your name: ")
    print(f"Hello, {name} and your type is {type(name)}")

if __name__ == "__main__":
    #for_in_loop()
    #print_dictionary()
    #while_loop_examle()
    #break_and_continue()
    #write_only_even_numbers()
    #learn_pass_statement()  
    #use_range_function()
    #use_range_function_with_step()
    #use_enumerate_function()
    #use_zip_function()
    #use_in_function()   
    use_input()