def sum_of_numbers(*args):
    return sum(args)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():   
        print(f"{key}: {value}")

def spy_game(nums):
    for num in nums:
        if num == 0:
            pass



if __name__ == "__main__":
    print(sum_of_numbers(1, 2, 3, 4, 5))
    print_kwargs(name="Mustafa", age=25, city="Istanbul")   
    spy_game([1,2,4,0,0,7,5])
    spy_game([1,0,2,4,0,5,7])
    spy_game([1,7,2,0,4,5,0])