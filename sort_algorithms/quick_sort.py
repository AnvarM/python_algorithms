import time
import big_array

#Quick Sort
def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        m = list[0]
        leser = []
        bigger = []
        equal = []
        for i in list:
            if i < m:
                leser.append(i)
            elif i > m:
                bigger.append(i)
            else:
                equal.append(i)
        return quick_sort(leser) + equal + quick_sort(bigger)

#Test Quick Sort Time
array = big_array.get_big_array()
start_time = time.process_time()
quick_sort(array)
print(time.process_time() - start_time)