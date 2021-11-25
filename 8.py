s = input("Введите строку ")

h1 = s.find('h')
h2 = s.rfind('h')

a1 =s[h1 - 1::]
a2 =s[h1 + 1:h2 - 1:-1]
a3 =s[h2 + 1::]
a4 = s[:h2 : - 1]


a = a3 + a4

print(a1)
print(a2)
print(a3)
print(a4)
print(a)