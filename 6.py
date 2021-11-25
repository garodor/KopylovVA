s = input("Введите строку ")

h = s.rfind('h') 

a = s[h + 1:]
b = s[:h:- 1]
print(a)
print(b)