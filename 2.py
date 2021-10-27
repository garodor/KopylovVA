def cicl(a,b,c):
    for i in range(a,b,c):
     print(i)

a = int(input("Введите число a "))
b = int(input("Введите число b "))
if a > b:
       cicl(a,b - 1, -2)

else:
       cicl(a,b + 1, 3)