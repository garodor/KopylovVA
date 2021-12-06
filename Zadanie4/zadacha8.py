# -- coding: utf-8 --
def vb():
   s = input("Введите строку: ")

   h1 = s.find('h')
   h2 = s.rfind('h') 
   a = s[h2 - 1:h1:- 1]
   print(a)

vb()