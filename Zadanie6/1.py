# -*- coding: utf-8 -*-

from tkinter import *

len  = 0
next = 0
pred = 0
max1 = 0
dano = ""




# кнопка1 начало  
def clicked1(): 
    n = int(txt.get())
    i = 1
    res = "Результат: "
    while i ** 2 <= n:
        res = res + str(i) + "; "
        i += 1    
    lbl.configure(text=res)
    
   
def window1():
    global txt, lbl 

    win = Tk()
    win.title("Задача №1")
    win.geometry("400x400")
    lb = Label(win, text="Введите целое число: ")  
    lb.grid(column=0, row=0) 
    txt = Entry(win,width=15)
    txt.grid(column=1, row=0)  
    b = Button(win, text="Вычислить", width=10, command=clicked1)
    b.grid(column=2, row=0)  
    lbl = Label(win, text="Результат: ")  
    lbl.grid(column=0, row=1) 
# кнопка1 окончание 

 
# кнопка2 начало  
def clicked2(): 
    n = int(txt.get())
    i = 2
    
    while n % i != 0:
        i += 1    
    res = "Результат: " + str(i)
    lbl.configure(text=res)
    
   
def window2():
    global txt, lbl 

    win = Tk()
    win.title("Задача №2")
    win.geometry("400x400")
    lb = Label(win, text="Введите целое число не меньше 2: ")  
    lb.grid(column=0, row=0) 
    txt = Entry(win,width=15)
    txt.grid(column=1, row=0)  
    b = Button(win, text="Вычислить", width=10, command=clicked2)
    b.grid(column=2, row=0)  
    lbl = Label(win, text="Результат: ")  
    lbl.grid(column=0, row=1) 
# кнопка2 окончание 



# кнопка3 начало  
def clicked3(): 
    n = int(txt.get())
    m = 0
    res = "Результат: "
    while 2 ** m < n:
        m += 1
    res = res + str(m - 1)        
    lbl.configure(text=res)
     
   
def window3():
    global txt, lbl 

    win = Tk()
    win.title("Задача №3")
    win.geometry("400x400")
    lb = Label(win, text="Введите натуральное число: ")  
    lb.grid(column=0, row=0) 
    txt = Entry(win,width=15)
    txt.grid(column=1, row=0)  
    b = Button(win, text="Вычислить",  width=10, command=clicked3)
    b.grid(column=2, row=0)  
    lbl = Label(win, text="Результат: ")  
    lbl.grid(column=0, row=1) 
# кнопка3 окончание 


# кнопка4 начало  
def clicked4(): 
    x = int(txt_x.get())
    y = int(txt_y.get())
    i = 1
    res = "Результат: "
    while x < y:
        x *= 1.1
        i += 1
    res = res + str(i)  
    lbl.configure(text=res)
     
   
def window4():
    global txt_x, txt_y, lbl

    win = Tk()
    win.title("Задача №4")
    win.geometry("400x400")
    lb_х = Label(win, text="Введите натуральное число х: ")  
    lb_х.grid(column=0, row=0) 
    txt_x = Entry(win,width=15)
    txt_x.grid(column=1, row=0) 
    lb_y = Label(win, text="Введите натуральное число y: ")  
    lb_y.grid(column=0, row=1) 
    txt_y = Entry(win,width=15)
    txt_y.grid(column=1, row=1) 
    b = Button(win, text="Вычислить", width=10, command=clicked4)
    b.grid(column=0, row=2)  
    lbl = Label(win, text="Результат: ")  
    lbl.grid(column=0, row=3) 
# кнопка4 окончание 


# кнопка5 начало  
def clicked5():
    global len, dano
    

    n = int(txt.get())
    txt.delete(0,END)

    if n != 0 :
        len = len + 1
        dano = dano + str(n) + "; "
    else:    
        res = "Результат: " + str(len)
        lbl.configure(text=res)
        l.configure(text=dano)
        len = 0
        dano = ""

    
   
def window5():
    global txt, lbl, l 
    
   
    win = Tk()
    win.title("Задача №5")
    win.geometry("500x400")
    lb = Label(win, text="Введите последовательность неотрицательных чисел ")  
    lb.grid(column=0, row=0) 
    txt = Entry(win,width=15)
    txt.grid(column=1, row=0)  
    b = Button(win, text="Ввод", width=10, command=clicked5)
    b.grid(column=2, row=0)  
    l = Label(win, text="")  
    l.grid(column=0, row=2) 
    lbl = Label(win, text="Результат: ")  
    lbl.grid(column=0, row=3) 
# кнопка5 окончание 


# кнопка6 начало  
def clicked6():
    global len, next, dano
    

    n = int(txt.get())
    txt.delete(0,END)
     
    if n != 0 :
        len = len + 1 
        next = next + n
        dano = dano + str(n) + "; "
    else:    
        res = "Результат: " + str(next / (len + 1))
        lbl.configure(text=res)
        l.configure(text=dano)
        len  = 0 
        next = 0
        dano = ""
   
def window6():
    global txt, lbl, l
    
   
    win = Tk()
    win.title("Задача №6")
    win.geometry("400x400")
    lb = Label(win, text="Введите последовательность чисел")  
    lb.grid(column=0, row=0) 
    txt = Entry(win,width=15)
    txt.grid(column=1, row=0)  
    b = Button(win, text="Ввод", width=10, command=clicked6)
    b.grid(column=2, row=0)  
    l = Label(win, text="")  
    l.grid(column=0, row=2) 
    lbl = Label(win, text="Результат: ")  
    lbl.grid(column=0, row=3) 
# кнопка6 окончание 

# кнопка7 начало  
def clicked7():
    global len, pred, dano
    

    n = int(txt.get())
    txt.delete(0,END)

    if n != 0 :
        if n > pred  :
            len = len + 1 
        pred = n
        dano = dano + str(n) + "; "
    else: 
        pred = 0   
        res = "Результат: " + str(len - 1)
        len = 0
        lbl.configure(text=res)
        l.configure(text=dano)
        dano = ""
    
   
def window7():
    global txt, lbl, l
    
   
    win = Tk()
    win.title("Задача №7")
    win.geometry("500x400")
    lb = Label(win, text="Введите последовательность натуральных чисел ")  
    lb.grid(column=0, row=0) 
    txt = Entry(win,width=15)
    txt.grid(column=1, row=0)  
    b = Button(win, text="Ввод", width=10, command=clicked7)
    b.grid(column=2, row=0)  
    l = Label(win, text="")  
    l.grid(column=0, row=2) 
    lbl = Label(win, text="Результат: ")  
    lbl.grid(column=0, row=3) 
# кнопка7 окончание 
    
    # кнопка8 начало  
def clicked8():
    global len, max1, pred, dano
    

    n = int(txt.get())
    txt.delete(0,END)

    if n != 0 :
        if n == pred  :
            len = len + 1 
        else: 
             pred = n
             max1 = max(max1, len)
             len = 0   
        dano = dano + str(n) + "; "   
    else: 
        max1 = max(max1, len)
        len = 0
        pred = 0   
        res = "Результат: " + str(max1 + 1)
        lbl.configure(text=res)
        l.configure(text=dano)
        max1 = 0
        dano = ""

    
   
def window8():
    global txt, lbl, l 
    
   
    win = Tk()
    win.title("Задача №8")
    win.geometry("500x400")
    lb = Label(win, text="Введите последовательность натуральных чисел ")  
    lb.grid(column=0, row=0) 
    txt = Entry(win,width=15)
    txt.grid(column=1, row=0)  
    b = Button(win, text="Ввод", width=10, command=clicked8)
    b.grid(column=2, row=0)  
    l = Label(win, text="")  
    l.grid(column=0, row=2) 
    lbl = Label(win, text="Результат: ")  
    lbl.grid(column=0, row=3) 
# кнопка8 окончание 


tk = Tk()
tk.title("Практическая работа №6")
tk.geometry("400x400")

b1 = Button(tk,text="Задание 1",background="#ffc0cb", height = "2",width = "15",command=window1)
b1.pack()

b2 = Button(tk,text="Задание 2",background="#ff0000", height = "2",width = "15",command=window2)
b2.pack()

b3 = Button(tk,text="Задание 3",background="#ff7d00", height = "2",width = "15",command=window3)
b3.pack()

b4 = Button(tk,text="Задание 4",background="#ffff00", height = "2",width = "15",command=window4)
b4.pack()

b5 = Button(tk,text="Задание 5",background="#00ff00", height = "2",width = "15",command=window5)
b5.pack()

b6 = Button(tk,text="Задание 6",background="#007dff", height = "2",width = "15",command=window6)
b6.pack()

b7 =  Button(tk,text="Задание 7",background="#0000ff", height = "2",width = "15",command=window7)
b7.pack()

b8 = Button(tk,text="Задание 8",background="#7d00ff", height = "2",width = "15",command=window8)
b8.pack()

tk.mainloop()