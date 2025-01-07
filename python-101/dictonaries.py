def dictionaries():
    my_dict = {"name": "Mustafa", "age": 25, "city": "Istanbul"}
    print(my_dict)
    print(my_dict["name"])
    my_dict["age"] = 26
    print(my_dict)
    my_dict["email"] = "mustafa@gmail.com"
    print(my_dict)

if __name__ == "__main__":
    dictionaries()