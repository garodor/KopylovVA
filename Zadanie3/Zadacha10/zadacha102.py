# -- coding: utf-8 --

N = int(input("Введите количество чисел N "))
K = int(input("Введите количество чисел K "))

if N == 1:
 sum = 1
elif N == 2:
        if  K == 1:
            sum = 2
        elif K == 2:
            sum = 1     
else:        
        if K == 1:
            sum = 2
        elif K == 2:
            sum = 1
        else:
            sum = 0    
        F1 = 1
        F2 = 1
        for i in range(3,N + 1): 
            F1,F2 = F2,F1 + F2 
            if i >= K:
             sum += F2

print(sum)

