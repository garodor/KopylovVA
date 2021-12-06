# -- coding: utf-8 --

def ravno(a,b,c):
    if a == b == c:
        return 3 
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0

a = float(input("Введите число a "))
b = float(input("Введите число b "))
c = float(input("Введите число c "))

d = ravno(a,b,c)

print(d)

