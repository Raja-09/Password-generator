
import random
import pyperclip as pc 
import tkinter as tk
from tkinter import ttk  

def check(pwd):
    sym= ['@','%',';','$','/','#','&']
    matched_list = [characters in sym for characters in pwd]
    check=all(matched_list)
    if(True in matched_list):
        return pwd 
    else:
        return pwd[:len(pwd)-1]+'@'
    # if('@' in pwd or '%' in pwd or ';' in pwd or '$' in pwd or '/' in pwd or '#' in pwd or '&' in pwd ):
    # if(sym in pwd):
    #     return pwd
    # else:
    #     return pwd[:len(pwd)-1]+'@'

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

root  = tk.Tk()
root.geometry("250x75")
root.iconbitmap(r'C:\Users\Raja Aravindha\Desktop\CSE\Projects\PasswordPy\icon1.ico')
root.eval('tk::PlaceWindow . center')
pwdval = tk.StringVar()
root.title("Password Generator")
def buttonfun():
    pwdval.set(pwdgen(10))
    # print(pwdval.get())
    pc.copy(pwdval.get())
    label.pack()

password = tk.Entry(root, textvariable = pwdval )
password.pack()
button = ttk.Button(root, text = "Genarate",command=lambda:buttonfun() )
button.pack()
label = tk.Label(root,text="Password has been copied")
root.mainloop()