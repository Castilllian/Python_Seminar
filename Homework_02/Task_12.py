# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введите число S: "))
p = int(input("Введите число P: "))
a = 1
b = -s
c = p
Dis = b**2-4*a*c
x_1 = (-b-Dis**(-0.5))/2*a
x_2 = (-b+Dis**(-0.5))/2*a
print(x_1, x_2)