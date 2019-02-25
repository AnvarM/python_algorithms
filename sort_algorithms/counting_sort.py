import big_array
import time

#Counting Sort
def counting_sort(array):
    counter = [0]*10
    sorted_array = []
    for i in array:
        counter[i] += 1
    for i in range(len(counter)):
        for j in range(counter[i]):
            sorted_array.append(i)

    return sorted_array

#Test Counting Sort Time
array = big_array.get_big_array_with_range_of_values()
start_time = time.process_time()
counting_sort(array)
print(time.process_time() - start_time)

