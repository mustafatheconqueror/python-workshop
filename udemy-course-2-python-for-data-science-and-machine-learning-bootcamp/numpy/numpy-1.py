import numpy as np

def create_simple_array():
    simple_array = np.arange(10)
    simple_array2 = np.arange(10, 20)
    simple_array3 = np.arange(10, 20, 2)
    print(f"type of simple_array: {type(simple_array)}")
    print(f"simple_array: {simple_array}")
    print(f"simple_array2: {simple_array2}")
    print(f"simple_array3: {simple_array3}")

def create_zero_matrix():
    zero_matrix = np.zeros(3)
    zero_matrix2 = np.zeros((3, 3)) # row x column
    print(f"zero_matrix: {zero_matrix} type: {type(zero_matrix)}")
    print(f"zero_matrix2: {zero_matrix2} type: {type(zero_matrix2)}")


def create_ones_matrix():
    ones_array = np.ones(3)
    ones_matrix = np.ones((3, 3))
    print(f"ones_array: {ones_array} type: {type(ones_array)}")
    print(f"ones_matrix: {ones_matrix} type: {type(ones_matrix)}")


def create_ln_space():
    ln_space = np.linspace(0, 10, 5)
    print(f"ln_space: {ln_space} type: {type(ln_space)}")

def create_identity_matrix():
    identity_matrix = np.eye(3)
    print(f"identity_matrix: {identity_matrix} type: {type(identity_matrix)}")

def create_random_one_dimensional_array():
    random_array = np.random.rand(3)
    print(f"random_array: {random_array} type: {type(random_array)}")

def create_random_two_dimensional_array():
    random_matrix = np.random.rand(3, 3)
    print(f"random_matrix: {random_matrix} type: {type(random_matrix)}")

def create_random_one_dimensional_array_with_n():
    random_array = np.random.randn(3)
    print(f"random_array: {random_array} type: {type(random_array)}")

def create_random_one_dimensional_with_random_int():
    random_int_array = np.random.randint(1, 10, 3)
    print(f"random_int_array: {random_int_array} type: {type(random_int_array)}")


def reshape_array():
    my_array = np.arange(9)
    my_array2 = my_array.reshape(3, 3)
    print(f"my_array2: {my_array2} type: {type(my_array2)}")


def find_max_index_in_array():
    my_array = np.random.randint(1, 10, 5)
    return my_array.argmax()


if __name__ == "__main__":
    #create_simple_array()
    #create_zero_matrix()
    #create_ones_matrix()
    #create_ln_space()
    #create_identity_matrix()
    #create_random_one_dimensional_array()
    #create_random_two_dimensional_array()
    #create_random_one_dimensional_array_with_n()
    #create_random_one_dimensional_with_random_int()
    #reshape_array()
    print(find_max_index_in_array())