# -- coding: utf-8 --

n = int(input("Введите количество минут n "))

a = 60 * 24

if n > a:
    print("Количество минут n недолжно превышать",a)
else: 
    ch = n // 60
    min = n % 60

    print(ch, ":", min)