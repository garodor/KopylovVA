# -- coding: utf-8 --
def vb():
    s = input("Введите строку, состоящую из двух слов, разделенных пробелом: ")

    p = s.find(' ')

    s1 = s[:p]
    s2 = s[p + 1:]

    a = s2 + " " + s1

    print(a)
    
vb()