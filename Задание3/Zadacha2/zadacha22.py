def funck(A1,B1,c):
    for i in range(A1,B1,c):
    
        print(i)
        

A = int(input("Введите число A "))
B = int(input("Введите число B "))

if A < B:
    funck(A,B + 1,1)
else:
    funck( A , B - 1, -1)  
