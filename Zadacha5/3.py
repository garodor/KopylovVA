n = int(input("Введите натуральное число "))
m = 0
while 2 ** m < n:
     m += 1
print (m-1)