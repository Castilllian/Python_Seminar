# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

num_1 = int(input("Введите первый элемент ариф-ой прогрессии: "))
num_2 = int(input("Введите разность ариф-ой прогрессии: "))
num_3 = int(input("Введите длину ариф-ой прогрессии: "))

array = []
for i in range(1, num_3):
    next_num = num_1 + (i-1)*num_2
    array.append(next_num)
print(array)