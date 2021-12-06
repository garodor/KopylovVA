# -- coding: utf-8 --
def prof():
    n = int(input("Введите целое число, не меньше 2: "))
    i = 2
    while n % i != 0:
        i += 1
    print(i)

prof()