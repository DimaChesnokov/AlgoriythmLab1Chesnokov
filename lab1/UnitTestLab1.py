import unittest
from Lab1 import gnome_sort  

#  unit-тесты для функции gnome_sort
class TestGnomeSort(unittest.TestCase):
    def setUp(self):
        #  данные для тестов
        self.sorted_arr = [1, 2, 3, 4, 5]
        self.reverse_arr = [5, 4, 3, 2, 1]
        self.random_arr = [3, 5, 1, 4, 2]
        self.empty_arr = []

    def test_sorted_array(self):
        # Проверяем, что функция правильно сортирует отсортированный массив
        self.assertEqual(gnome_sort(self.sorted_arr), sorted(self.sorted_arr))

    def test_reverse_sorted_array(self):
        # Проверяем, что функция правильно сортирует обратно отсортированный массив
        self.assertEqual(gnome_sort(self.reverse_arr), sorted(self.reverse_arr))

    def test_random_array(self):
        # Проверяем, что функция правильно сортирует случайный массив
        self.assertEqual(gnome_sort(self.random_arr), sorted(self.random_arr))

    def test_empty_array(self):
        # Проверяем, что функция корректно обрабатывает пустой массив
        self.assertEqual(gnome_sort(self.empty_arr), [])

if __name__ == '__main__':
    unittest.main()