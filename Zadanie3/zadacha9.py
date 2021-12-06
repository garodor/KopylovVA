# -- coding: utf-8 --

n = int(input("Введите количество чисел n "))

if n == 1:
    sum = 1
else:
    F1 = 1
    F2 = 1

    sum = F1 + F2
    for i in range(n - 2): 
        F1,F2 = F2, F1 + F2 
        sum += F2 
print(sum)