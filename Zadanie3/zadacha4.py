# -- coding: utf-8 --

n = int(input("Введите количество чисел n "))

sum = 0
for i in range(1,n + 1):
    a = int(input("Введите целое число "))
    sum += a 
print(sum)