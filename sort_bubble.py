import timeit

# Массив для сортировки
mas = [
    48, 16, 22, 32, 32, 40, 85, 90, 117, 130, 150, 165, 182, 191, 192, 194, 226, 227, 227, 273,
    276, 291, 296, 315, 320, 324, 94, 328, 342, 348, 352, 362, 372, 392, 113, 401, 405, 420, 424,
    433, 448, 452, 1, 481, 484, 490, 11, 493, 66, 508, 512, 12, 536, 537, 540, 540, 565, 569,
    571, 585, 586, 598, 10, 605, 622, 623, 627, 637, 643, 6, 649, 655, 664, 668, 48, 675, 685,
    685, 686, 693, 710, 52, 729, 748, 751, 760, 808, 809, 811, 819, 831, 56, 917, 921, 924, 928,
    928, 958, 996, 3
]

# Функция быстрой сортировки
def quick_sort(s):
    if len(s) <= 1:
        return s

    element = s[0]  # Опорный элемент
    left = list(filter(lambda i: i < element, s))  # Меньше опорного
    center = [i for i in s if i == element]  # Равные опорному
    right = list(filter(lambda i: i > element, s))  # Больше опорного

    return quick_sort(left) + center + quick_sort(right)

# Функция сортировки пузырьком
def bubble_sort():
    mas_copy = mas.copy()  # Создаем копию массива для сортировки пузырьком
    n = len(mas_copy)
    for run in range(n-1):
        for i in range(n-1-run):
            if mas_copy[i] > mas_copy[i + 1]:
                mas_copy[i], mas_copy[i + 1] = mas_copy[i + 1], mas_copy[i]
    return mas_copy

# Функция сортировки выбором
def selection_sort(arr):
    # Проходим по всему списку
    for i in range(len(arr)):
        # Предполагаем, что первый элемент в неотсортированной части - это минимальный
        min_index = i
        # Ищем минимальный элемент в оставшейся части списка
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Меняем местами найденный минимальный элемент с первым элементом в неотсортированной части
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Измерение времени работы быстрой сортировки
quick_sort_time = timeit.timeit(lambda: quick_sort(mas), number=1)
print(f"Время работы быстрой сортировки: {quick_sort_time} секунд")

# Измерение времени работы сортировки пузырьком
bubble_sort_time = timeit.timeit(bubble_sort, number=1)
print(f"Время работы сортировки пузырьком: {bubble_sort_time} секунд")

# Измерение времени работы сортировки выбором
selection_sort_time = timeit.timeit(lambda: selection_sort(mas.copy()), number=1)  # Копия массива, чтобы не менять оригинал
print(f"Время работы сортировки выбором: {selection_sort_time} секунд")


