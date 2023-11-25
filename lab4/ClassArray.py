# Определяем функцию гномьей сортировки.
#Суть: проходит по массиву с помощью указателя и сравнивает текущий с предыдущим. Если текущий больше или равен предыдущиму, то указатель сдвигается  на след. эл.,
#иначе они меняются местами и указатель сдвигается на предыдущий элемент. До конца массива повторяется.
#Сложность алгоритма  составляет O(n^2).
def gnome_sort(arr):
    i = 1
    # Запускаем цикл, который будет выполняться до тех пор, пока i меньше длины массива arr
    while i < len(arr):
        # Если i равно 0, то устанавливаем i равным.
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