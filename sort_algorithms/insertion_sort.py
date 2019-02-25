import time
import big_array

# Сортировка вставками, берет элемент(ключ), сохраняет в переменную и сравнивает следующие элементы с этим элементом,
# если следующий элемент меньше, то элемент ставится на позицию ниже и так далее, пока не встретится элемент больше
# ключа, здесь ключ ставится на место предыдущего перенесенного элемента и цикл начинается со следующим элементом


def insertion_sort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

# Проверка работы по времени для массива с 500000 элементами
array = big_array.get_big_array()
start_time = time.process_time()
insertion_sort(array)
print(time.process_time() - start_time)