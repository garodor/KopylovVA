print("Курс основы программирования начался")

a=16823 * 12302%3092

print(a)

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

    seconds = int(input("Введите количество секунд "))

d     = seconds 
ost_d = seconds 

ch    = ost_d 
ost_ch = ost_d % 3600

m      = ost_ch 
s  = ost_ch % 60

print(d,":", ch,":", m,":",s)

n = int(input("Введите число n "))

print(n+n**2+n**3+n**4+n**5)

x = input("Введите x ")
y = input("Введите y ")

x,y=y,x
print("x =",x)
print("y =",y)

number = int(input("Введите целое число "))

ostatok = number%2
if ostatok == 0:
    print("Число",number,"четное")
else:
    print("Число",number,"нечетное")
