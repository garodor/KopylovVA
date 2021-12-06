# -- coding: utf-8 --
def prof():
    n = int(input("Введите последовотельность натуральных чисел "))
    a = 0
    while n != 0:
        next = int(input())
        if n < next:
            a += 1
        n = next
    print("Ответ:", a)

prof()