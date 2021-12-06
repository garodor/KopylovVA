# -- coding: utf-8 --

n = int(input("Введите число n "))

pr = 1 
for i in range(1, n + 1):
    pr *= i
print(pr)