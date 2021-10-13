a = int(input("Введите число a "))
b = int(input("Введите число b "))

a,b = b,a + b
if a > b:
    for i in range (a,b - 1, -2):
        print(i)
else:
    for i in range(a,b + 1):
        print(i)