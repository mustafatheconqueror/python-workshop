def logical_comparasion():
    a = 10
    b = 20
    print(a == b)
    print(a != b)
    print(a > b)
    print(a < b)
    print(a >= b)
    print(a <= b)

    if a == b or a > b:
        print("a is equal to b or a is greater than b")
    else:
        print("a is not equal to b and a is not greater than b")

    if not (a == b) : 
        print("a is not equal to b")
    else:
        print("a is equal to b")    


if __name__ == "__main__":
    logical_comparasion()