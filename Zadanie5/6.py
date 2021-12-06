# -- coding: utf-8 --
def prof():
    n    = int(input("Введите последовотельность натуральных чисел "))
    a    = 1
    next = 1
    while next != 0:
      next = int(input())
      a += 1
      n += next

    print("Ответ:", n / a )

prof()