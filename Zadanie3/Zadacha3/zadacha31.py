# -- coding: utf-8 --
def vi():

   A = int(input("Введите число A "))
   B = int(input("Введите число B "))

   if A % 2 == 0:
       for i in range(A - 1, B - 1, -2):
           print(i)
   else:
     for i in range(A, B - 1, -2):
       print(i)  

vi()   