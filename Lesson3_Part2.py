import numpy as np
# Сумма ряда 0-100
array = np.arange(101)
print("Сумма ряда [0-100] = ", array.sum())
# Сумма ряда 0-input()
n = int(input("Введите значение N, для определения суммы ряда [0-N]\nN = "))
in_array = np.arange(n + 1)
print("Сумма ряда [0-", n, "] = ", in_array.sum(), sep='')
# Среднее среди 100 случаных чисел
random_array = np.random.randint(1, 1000, 100)
print(random_array)
print("Среднее среди 100 случаных чисел =", random_array.mean())