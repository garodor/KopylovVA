# -- coding: utf-8 --
def prof():
   x = int(input("Введите натуральное число "))
   y = int(input("Введите натуральное число "))
   i = 1
   while x < y:
       x *= 1.1
       i += 1
   print(i)

prof()