
import random
import pyperclip as pc 
import tkinter as tk
from tkinter import ttk  

def check(pwd):
    lower='abcdefghijklmnopqrstuvwxyz'
    upper=lower.upper()
    number='01234567890123456789'
    sym='@#$&/;%@#$&/;%'
    sym=    list(sym)
    lower=  list(lower)
    upper = list(upper)
    number = list(number)
    matched_list1 = [characters in sym for characters in pwd]
    matched_list2 = [characters in upper for characters in pwd]
    matched_list3 = [characters in lower for characters in pwd]
    matched_list4 = [characters in number for characters in pwd]


    if(True in matched_list1 and True in matched_list2 and True in matched_list3 and True in matched_list4):
        return pwd 
    else:
        return pwd[:len(pwd)-4]+sym[random.randint()]+upper[random.randint()]+lower[random.randint()]+number[random.randint()]
    
def pwdgen(num):
    lower='abcdefghijklmnopqrstuvwxyz'
    upper=lower.upper()
    number='01234567890123456789'
    sym='@#$&/;%@#$&/;%'

    all=upper+lower+number+sym
    # length=int(input("Enter the length of password: "))
    length = num
    pwd="".join(random.sample(all,length))
    # print(check(pwd,length))
    return(check(pwd))

def buttonfun():
    pwdval.set(pwdgen(15))
    # print(pwdval.get())
    pc.copy(pwdval.get())
    label.pack()

root  = tk.Tk()
root.geometry("250x75")
root.iconbitmap(r'.\icon1.ico')
root.eval('tk::PlaceWindow . center')
pwdval = tk.StringVar()
root.title("Password Generator")

password = tk.Entry(root, textvariable = pwdval )
password.pack()
button = ttk.Button(root, text = "Genarate",command=lambda:buttonfun() )
button.pack()
label = tk.Label(root,text="Password has been copied")
root.mainloop()
