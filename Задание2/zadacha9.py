def eda(n,m,k):
    if k < n * m :
        return "ДА"
    else:
        return "НЕТ"

n = float(input("Введите число n "))
m = float(input("Введите число m "))
k = float(input("Введите число k "))

d = eda(n,m,k)

print(d)