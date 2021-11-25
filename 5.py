s = input("Введите строку ")

h = s.find('h')

a = s[h - 1:: - 1]
b = s[:h]


print(b)
print(a)