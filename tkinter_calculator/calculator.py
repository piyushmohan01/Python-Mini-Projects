import mysql.connector

db = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = "root_password",
    database = "calclog"
)

mycursor = db.cursor()

q = "ALTER TABLE logs AUTO_INCREMENT=1"
mycursor.execute(q)
r = "TRUNCATE TABLE logs"
mycursor.execute(r)

    
def insert_action(v1,v2,v3,v4,v5):
    insertvar = "INSERT INTO logs (Num_1, Op_flag, Op_symbol, Num_2, Result) VALUES (%s, %s, %s, %s, %s)"
    val = (v1,v2,v3,v4,v5)
    print("RECORD ADDED!\n")
    mycursor.execute(insertvar, val)
    db.commit()


#------------------------------------------------------------------------------------------------------------------------------#

    
    
import tkinter as tk
import math as math
from tkinter import font as tkFont
from tkinter import *
from IPython import get_ipython

print("\n-----------CALCULATOR OPENED--------------\n")

window = tk.Tk()

window.title("GUI-Calculator") 
window['bg'] = 'lightblue'

helv36 = tkFont.Font(family='Trebuchet MS', size=30, weight=tkFont.BOLD)

cal_window = tk.Frame(window, borderwidth=0, relief='flat')
cal_window.pack()

textbox = tk.Entry(cal_window, width=13, bd=7.5, font=helv36)
textbox.grid(row=0,column=0)


def addText(n):
    number = int(n)
    textbox.insert(tk.END,number)

def deleteText(n):
    textbox.delete(0,tk.END)
    print("\n-----------------CLEAR--------------------\n")
    
def backSpace(n):
    txt = tk.Entry.get(textbox)[:-1]
    textbox.delete(0,tk.END)
    textbox.insert(0,txt)
        
li_op = ['+','-','x','/','%','log_','^']
    
def doFunc(n):
    global op 
    global symb
    op = n
    first_num = textbox.get()
    global f_num
    f_num = float(first_num)
    if op!=6:
        textbox.delete(0, tk.END)
        symb = li_op[op-1]
        textbox.insert(0,symb)
    if op==6:
        symb = 'log_'
        textbox.insert(0,symb)
    global v3
    v3 = symb
        
def printRes():
    global sec_num
    sec_get = textbox.get()
    if op!=6:
        sec_num = sec_get[1:]
    else:
        sec_num = sec_get[4:]
    textbox.delete(0, tk.END)
    print("1.ADD/2.SUB/3.MUL/4.DIV/5.REM/6.LOG/7.POW")
    print("\n   --   First Num: {0}".format(f_num))
    global v1 
    v1 = f_num
    print("   --   Operation Flag: {0}".format(op))
    global v2
    v2 = op
    print("   --   Second Num: {0}".format(sec_num))
    global v4
    v4 = sec_num
    li = []
    li.append(float(sec_num))
    for i in li:
        if op == 1:
            textbox.insert(0,f_num+i)
            break
        elif op == 2:
            textbox.insert(0,f_num-i)
            break
        elif op == 3:
            textbox.insert(0,f_num*i)
            break
        elif op == 4:
            textbox.insert(0,float(f_num/i))
            break
        elif op == 5:
            textbox.insert(0,float(f_num%i))
            break
        elif op == 6:
            textbox.insert(0,float(math.log(i)))
            break
        elif op == 7:
            textbox.insert(0,float(pow(f_num,i)))
            break
    res = textbox.get()
    print("   --   Final Result: {0}\n".format(res))
    global v5 
    v5 = res
    insert_action(v1,v2,v3,v4,v5)
    
new_frame = tk.Frame(window, borderwidth=10, relief='groove')
new_frame.pack()
num_clear = tk.Button(new_frame, text = "C", font=helv36, width=2,relief='flat', padx=10, command= lambda: deleteText(1))
num_log = tk.Button(new_frame, text = "log",font=helv36, width=2,relief='flat', padx=10, command= lambda: doFunc(6))
num_eq = tk.Button(new_frame, text = "=",font=helv36, width=2,relief='flat', padx=10, command= printRes)
num_del = tk.Button(new_frame, text = "D", padx=10,font=helv36, width=2,relief='flat', command= lambda: backSpace(0))
    
master = tk.Frame(window, borderwidth=10, relief='groove')
master.pack()

num_1 = tk.Button(master, text = "1", padx=10,font=helv36, width=2,relief='flat', command= lambda: addText(1))
num_2 = tk.Button(master, text = "2", padx=10,font=helv36, width=2,relief='flat', command= lambda: addText(2))
num_3 = tk.Button(master, text = "3", padx=10,font=helv36, width=2,relief='flat', command= lambda: addText(3))
num_4 = tk.Button(master, text = "4", padx=10,font=helv36, width=2,relief='flat', command= lambda: addText(4))
num_5 = tk.Button(master, text = "5", padx=10,font=helv36, width=2,relief='flat', command= lambda: addText(5))
num_6 = tk.Button(master, text = "6", padx=10,font=helv36, width=2,relief='flat', command= lambda: addText(6))
num_7 = tk.Button(master, text = "7", padx=10,font=helv36, width=2,relief='flat', command= lambda: addText(7))
num_8 = tk.Button(master, text = "8", padx=10,font=helv36, width=2,relief='flat', command= lambda: addText(8))
num_9 = tk.Button(master, text = "9", padx=10,font=helv36, width=2,relief='flat', command= lambda: addText(9))
num_0 = tk.Button(master, text = "0", padx=10,font=helv36, width=2,relief='flat', command= lambda: addText(0))

num_plus = tk.Button(master, text = "+", padx=10,font=helv36, width=2,relief='flat', command= lambda: doFunc(1))
num_minus = tk.Button(master, text = "-", padx=10,font=helv36, width=2,relief='flat', command= lambda: doFunc(2))
num_mul = tk.Button(master, text = "x", padx=10,font=helv36, width=2,relief='flat', command= lambda: doFunc(3))
num_div = tk.Button(master, text = "/", padx=10,font=helv36, width=2,relief='flat', command= lambda: doFunc(4))
num_per = tk.Button(master, text = "%", padx=10,font=helv36, width=2,relief='flat', command= lambda: doFunc(5))
num_pow = tk.Button(master, text = "^", padx=10,font=helv36, width=2,relief='flat', command= lambda: doFunc(7))

num_1.grid(row=4, column=2)
num_2.grid(row=4, column=3)
num_3.grid(row=4, column=4)
num_4.grid(row=3, column=2)
num_5.grid(row=3, column=3)
num_6.grid(row=3, column=4)
num_7.grid(row=2, column=2)
num_8.grid(row=2, column=3)
num_9.grid(row=2, column=4)
num_0.grid(row=5, column=3)
num_per.grid(row=5, column=4)
num_plus.grid(row=2, column=5)
num_minus.grid(row=3, column=5)
num_mul.grid(row=4, column=5)
num_div.grid(row=5, column=5)
num_pow.grid(row=5, column=2)
num_clear.grid(row=1,column=1)
num_del.grid(row=1, column=2)
num_log.grid(row=1,column=3)
num_eq.grid(row=1, column=4)

num_clear['bg'] = 'lightpink'
num_log['bg'] = 'lightpink'
num_del['bg'] = 'lightpink'
num_eq['bg'] = 'lightpink'
num_plus['bg'] = 'lightpink'
num_minus['bg'] = 'lightpink'
num_mul['bg'] = 'lightpink'
num_div['bg'] = 'lightpink'

window.mainloop()
print("\n-----------CALCULATOR CLOSED--------------\n")