def learn_map_func(numbers):
    for result in map(is_even, numbers):
        print(result)

def learn_filter_func(numbers):
    for result in filter(is_even, numbers):
        print(result)

def is_even(number):
    return number % 2 == 0


def learn_map_func_2():
    numbers = [1, 2, 3, 4, 5]
    result = map(lambda x : x * 2, numbers)
    for old_value, new_value in zip(numbers, result):
        print(f"Old value: {old_value}, New value: {new_value}")

def learn_filter_func_2():
    numbers = [1, 2, 3, 4, 5]
    result = filter(lambda x : x % 2 == 0, numbers)
    for old_value, new_value in zip(numbers, result):
        print(f"Old value: {old_value}, New value: {new_value}")


if __name__ == "__main__":
    learn_map_func([1, 2, 3, 4, 5])
    learn_filter_func([1, 2, 3, 4, 5])

    lambda_value = lambda x : x * 2
    print(lambda_value(2))
    learn_map_func_2()
    learn_filter_func_2()