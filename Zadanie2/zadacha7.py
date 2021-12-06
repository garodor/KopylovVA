# -- coding: utf-8 --

def vesok(a):
    if (a % 4 == 0 and not(a % 100) == 0) or (a % 400 == 0):
        return "ДА"
    else:
        return "НЕТ"  


god = int(input("Введите год "))

otvet = vesok(god)

print(otvet)