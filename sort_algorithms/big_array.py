import random
def get_big_array():
    big_array = []
    for i in range(499999):
         big_array.append(int(random.random()*499999))

    return big_array

def get_big_array_with_range_of_values():
    big_array = []
    for i in range(499999):
        big_array.append(random.randint(0,9)) # integers will be [0..9]

    return big_array
