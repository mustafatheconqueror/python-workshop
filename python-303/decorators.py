#let's return function from function
def return_function():
    print("Hello from return_function")
    def inner_function():
        print("Hello from inner_function")
    
    return inner_function


#passing function as argument
def pass_function(func):
    print("Hello from pass_function")
    func()

def hello():
    print("Hello from hello funciton")


def new_decorator(func):
    def new_function():
        func()
        print("Add new functionality")
    return new_function


@new_decorator # ı gain new functionality
def simple_function():
    print("Hello from simple_function")


if __name__ == "__main__":
    #my_function = return_function()
    #my_function() #you have to call the function like this  
    #pass_function(hello)
    simple_function()