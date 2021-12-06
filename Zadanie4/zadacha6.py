# -- coding: utf-8 --

s = input("Введите строку: ")

if s.count ('f') == 1:
    print(-1)

elif s.count ('f') < 1:
    print(-2)

else:
   a = s.find('f') + 1
   print(s.find('f',a))

   

