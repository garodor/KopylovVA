def otchot(A,B,c):
        for i in range(A,B,c):
            print(i)

A = int(input("Введите число A "))
B = int(input("Введите число B "))
if A % 2 == 0:
    otchot(A - 1, B - 1, -2)
else:
    otchot(A, B - 1, -2)