# -- coding: utf-8 --
def prof():
    a = 0
    max1 = 0
    b = 0

    n = int(input("Введите последовательность натуральных чисел "))
    while n != 0:
        if n == a:
            b += 1
        else:
            a = n
            max1 = max(max1, b)
            b = 0    
        n = int(input())
    max1 = max(max1, b)
    if max1 != 0:
        max1 = max1 + 1    
    print('Наибольшее число подряд идущих ',max1)

prof()