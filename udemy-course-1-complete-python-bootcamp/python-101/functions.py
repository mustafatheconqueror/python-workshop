def my_hello_function(name):
    print(f"Hello, {name}!")

def my_hello_function_with_default_value(name="Mustafa"):
    print(f"Hello, {name}!")

def sum_of_two_numbers(a, b):
    return a + b

def check_any_even_number(numbers):
    for number in numbers:
        if number % 2 == 0:
            return True
    return False

def employee_of_month(employees):
    max_hours = 0
    employee_of_month = ""
    for employee, hours in employees:
        if hours > max_hours:
            max_hours = hours
            employee_of_month = employee

    return (employee_of_month, max_hours)    
    


if __name__ == "__main__":
    #my_hello_function("Mustafa")
    #my_hello_function_with_default_value()
    #print(sum_of_two_numbers(1, 2))
    #print(check_any_even_number([1, 3, 5, 7, 9]))
    employess = [('Mustafa', 400), ('Kadir', 500), ('Zeyenep', 600)]
    employee, hours = employee_of_month(employess)
    print(f"Employee of the month is {employee} with {hours} hours")