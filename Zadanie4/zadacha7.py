# -- coding: utf-8 --
def vb():
   s = input("Введите строку: ")

   a = s.find('h')
   b = s.rfind('h')

   s1 = s[:a]
   s2 = s[b + 1:]

   print(s1 + s2)

vb()