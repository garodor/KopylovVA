# -- coding: utf-8 --
def vb():

    s = input("Введите строку: ")

    dlinas = len(s)

    dlinas2 = dlinas // 2

    dlinas1 = dlinas - dlinas2

    s1 = s[:dlinas1]
    s2 = s[dlinas1:]

    p = s2 + s1
 
    print(p)

vb()