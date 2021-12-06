# -- coding: utf-8 --

seconds = int(input("Введите количество секунд "))

d     = seconds // (24 * 60 * 60)  
ost_d = seconds - d * (24 * 60 * 60)

ch    = ost_d // (60 * 60)
ost_ch = ost_d - ch * (60 * 60)

m      = ost_ch // 60 
s  = ost_ch - m * 60

print(d,":", ch,":", m,":",s)