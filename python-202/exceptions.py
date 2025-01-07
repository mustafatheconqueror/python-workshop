def divide_by_zero():
    try: 
        print(10 / 0)
    except ZeroDivisionError:
        print("You cannot divide by zero")

def custom_exception(number):
    try:
        print(number / 0)
    except Exception as e:
        print(f" your erro is {e}")


def run_finally():
    try:
        print(10/0)
    except ZeroDivisionError:
        print("You cannot divide by zero")
    finally:
        print("This is finally block")

def example_func():
    while True:
        try:
            number = int(input("Enter a number:"))
            print(f"Congrats Your Number type is : {type(number)}")
        except Exception as e:
            print(f"Your error is {e}")
        else:
            print("You entered a number")
            break
        finally:
            print("This is finally block")

if __name__ == "__main__":
    #divide_by_zero()
    #custom_exception(10)
    #run_finally()
    example_func()
