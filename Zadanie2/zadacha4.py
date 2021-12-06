# -- coding: utf-8 --

def dlina(a,b,L,N):
     return  2 * L + 2 * b * (N - 1) + a * (2 * N - 1) 

a = float(input("Введите длину a "))
b = float(input("Введите длину b "))
L = float(input("Введите длину L "))
N = int(input("Введите количество отверстий в одном ряду N "))

d = dlina(a,b,L,N)

print(d)


