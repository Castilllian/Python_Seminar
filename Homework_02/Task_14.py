# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N
n = int(input("Введите число: "))
for i in range(1,n+1):
    count = 2
    if count < n:
        count = pow(count,i)
    if count >= n:
        break
    print(count)