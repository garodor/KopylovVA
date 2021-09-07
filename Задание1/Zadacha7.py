number = float(input("Введите целое число "))

ostatok = number%2
if ostatok == 0:
    print("Число",number,"четное")
else:
    print("Число",number,"нечетное")