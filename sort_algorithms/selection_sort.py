import time
import big_array

# Сортировка выбором, ищет наименьший элемент массива, меняет местами первый элемент и наименьший, далее последовательно
# меняет местами следующие наименьшие элементы из оставшихся
# Selection Sort search for element with minimum value and when find such element, swap this element with first element,
# then repeat this process for second element, third ...
def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(min+1,len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array


# Test Selection Sort Time
array = big_array.get_big_array()
start_time = time.process_time()
selection_sort(array)
print(time.process_time() - start_time)