# -- coding: utf-8 --

def chet(d):
    if d % 2 == 0:
        return "четное"
    else: 
        return "нечетное"  


def kletka(a,b):
    if (chet(a) == "нечетное" and chet(b) == "нечетное") or (chet(a) == "четное" and chet(b) == "четное"): 
        return "черная"
    else:
        return "белая"    
    
     
a1 = int(input("Введиде а1 "))
b1 = int(input("Введиде в1 "))
a2 = int(input("Введиде а2 "))
b2 = int(input("Введиде в2 "))

if kletka(a1,b1) == kletka(a2,b2):
    print("ДА")
else:
    print("НЕТ")
