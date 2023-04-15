# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

array = []
n = int(input("Введите количество элементов в массиве: "))
num = int(input('Введите число: '))

for i in range(n):
    elem = int(input("Введите элемент: "))
    array.append(elem)

closest = array[0]
for j in range(1, n):
    if abs(array[j] - num) < abs(closest - num):
        closest = array[j]

print(closest)
