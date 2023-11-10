import matplotlib.pyplot as plt
import numpy as np

class QuadraticFunction:
    def __init__(self, k, m, l):
        self.k = k
        self.m = m
        self.l = l

    def calculate(self, x):
        return self.k * x**2 + self.m * x + self.l
    
    

   

if __name__ == "__main__":
     # Заданные значения
    k =1 #int(input("Введите значение K: "))
    m =1 #int(input("Введите значение m: "))
    l =0 #int(input("Введите значение l: "))
    print("параметр 'a'  должен быть больше параметра 'b'")
    a = -1 #int(input("Введите значение a: ")) #пример с задания: a = -1; b = 1 h = 0,05
    b = 1 #int(input("Введите значение b: "))
    if a > b: 
        print("параметр 'a' не должен быть больше параметра 'b'")
        exit()
    h = 0.05 #float(input("Введите значение h: "))

    # Создаем объект класса QuadraticFunction
    quadratic_function = QuadraticFunction(k, m, l)

     # Создаем списки для значений x и y
    x_values = np.arange(a, b + h, h)
    y_values = [quadratic_function.calculate(x) for x in x_values]
    print("f(x) = kx^2 + mx + l")
    # Вывод таблицы значений
    print("x\tf(x)")
    x = a
    while x <= b:
        y = quadratic_function.calculate(x)
        print(f"{x:.2f}\t{y:.2f}")
        x += h
    
     # Построение графика
    plt.plot(x_values, y_values, label=f"f(x) = {k}x^2 + {m}x + {l}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("График функции f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
        
        
        

        