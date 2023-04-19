# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит в строку первый список затем на следующией строке второй список.

list_1 = []
list_2 = []
list_3 = []
n = int(input("Введите количество элементов в первом массиве: "))
m = int(input("Введите количество элементов во втором массиве: "))

for i in range(n):
    elem = int(input("Введите элемент: "))
    list_1.append(elem)
print(list_1)

for j in range(m):
    elem = int(input("Введите элемент: "))
    list_2.append(elem)
print(list_2)

for i in range(len(list_1)):
    for j in range(len(list_2)):
        if list_1[i] == list_2[j]:
            list_3.append(list_1[i])

list_3.sort()
print(list_3)