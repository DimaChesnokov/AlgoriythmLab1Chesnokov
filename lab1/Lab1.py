
import random,time
# Определяем функцию гномьей сортировки
def gnome_sort(arr):
    i = 1
    # Запускаем цикл, который будет выполняться до тех пор, пока i меньше длины массива arr
    while i < len(arr):
        # Если i равно 0, то устанавливаем i равным 
        if i == 0:
            i = 1
        # Если элемент на позиции i больше или равен элементу на позиции i-1, то увеличиваем i на 1
        if arr[i] >= arr[i-1]:
            i += 1
         # Если элемент на позиции i меньше элемента на позиции i-1, то меняем их местами и уменьшаем i на 1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    return arr

# Запрашиваем имена файлов для ввода и вывода данных у пользователя
input_file = input("Введите имя файла с входными данными: ")
output_file = input("Введите имя файла для вывода результата: ")


# Генерируем count случайных чисел и записываем их в файл для ввода данных
count = int(input("Введите количество случайных чисел в файле: "))
with open(input_file, "w") as f:
    for i in range(count):
        f.write(str(random.randint(1, 100)) + "\n")

# Открываем файл для чтения и считываем данные в список arr
with open(input_file, "r") as f:
    data = f.read().splitlines()
    arr = [int(x) for x in data]

# засечение времени начала сортировки
start_time = time.time()

# Вызываем функцию гномьей сортировки для сортировки списка
# и сохраняем результат в файл для вывода данных
sorted_arr = gnome_sort(arr)

# засечение времени окончания сортировки
end_time = time.time()

with open(output_file, "w") as f:
    for num in sorted_arr:
        f.write(str(num) + "\n")

# вычисление времени работы сортировки
sort_time = end_time - start_time

print(f"Время работы сортировки: {sort_time} секунд")

# Выводим сообщение о том, что результат работы программы сохранен в файле для вывода данных
print("Результат работы программы сохранен в файл", output_file)

