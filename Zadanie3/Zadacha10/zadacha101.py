# -- coding: utf-8 --

def cikl(M):
    if M == 1:
        sum = 1
    else:
        F1 = 1
        F2 = 1
        sum = F1 + F2
        for i in range(M - 2): 
            F1,F2 = F2, F1 + F2 
            sum += F2 
    return sum

N = int(input("Введите количество чисел N "))
K = int(input("Введите количество чисел K "))

sumN = cikl(N)
sumK = cikl(K)

sumKN = sumN - sumK 

print(sumKN)









    
    
    
    
