seconds = int(input("Введите количество секунд "))

d     = seconds 
ost_d = seconds 

ch    = ost_d 
ost_ch = ost_d % 3600

m      = ost_ch 
s  = ost_ch % 60

print(d,":", ch,":", m,":",s)