s = input("Введите строку ")

h1 = s.find('h')
h2 = s.rfind('h')

a1 = s [:h1]
a2 =s[h2 - 1:h1: - 1]
a3 = s[h2 + 1:]
a = a1 + a2 + a3

print(a)