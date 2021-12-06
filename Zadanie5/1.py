# -- coding: utf-8 --

def prof():
    n = int(input("Введите целое число "))
    i = 1
    while i ** 2 <= n:
       print(i ** 2)
       i += 1

prof()    