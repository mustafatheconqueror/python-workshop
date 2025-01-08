
def simple_function():
    return range(3)


if __name__ == "__main__":
    print(type(simple_function()))
    for i in simple_function():
        print(i)

