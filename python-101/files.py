def files():
    file = open("deneme.txt")
    print(file.read()) # when read is called, the file pointer is at the end of the file
    print("s" + file.read())
    file.seek(0) # moves the file pointer to the beginning of the file
    print(file.read())
    file.close()

def read_lines():
    my_file = open("deneme.txt")
    print(my_file.readlines())
    my_file.close()


def file_with_open_context_manager():
    with open("deneme.txt") as my_file:
        print(my_file.readlines())

def file_with_mode():
    with open("deneme.txt", "w+") as my_file:
        my_file.write("Writing new content to the file")
        my_file.seek(0)
        print(my_file.read())


if __name__ == "__main__":
    #files()
    #read_lines()
    #file_with_open_context_manager()
    file_with_mode()
    