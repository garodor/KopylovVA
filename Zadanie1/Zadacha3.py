# -- coding: utf-8 --

name = input("Введите Ваше имя ")
age  = int(input("Введите Ваш возраст "))

if age > 0 and age < 75:
    if age >= 16:
        print("Поздравляем, Вы поступили во ВГУИТ!")
    else:
        ost = 17 - age 
        print("Вам осталось учится",ost,"г.")
        print("Сначала нужно окончить школу!")
else:
    print("Вы ввели некорректный возраст")
    
if name == "Иван":
    print("Ваше имя Иван")
else:
    print("Ваше имя не Иван")
