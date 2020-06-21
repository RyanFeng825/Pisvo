"""
    Name   : Py
    To     : Python2
    Plat   : Windows7-SP1
    Lan    : Python2
    Time   : 2020-01-24
    Author : Ryan
"""
#GUI
import win32api, win32gui
ct = win32api.GetConsoleTitle()
hd = win32gui.FindWindow(0,ct)
win32gui.ShowWindow(hd,0)

#import
import subprocess
import os
import sys
import time
import tkinter as tk
from tkinter import messagebox

#welcome
messagebox.showinfo("Welcome","Welcome to use Py-0.0.1")
time.sleep(1)
#enter
messagebox.showwarning("Caution","We will start soon!")
time.sleep(2)

#get infomation_bool
plat_bool = messagebox.askquestion("Platform","Whether Python2")

window_nq = tk.Tk()
entry_text = tk.Entry(window_nq,width=40)
entry_text.pack()
def change_state():
    global var_string
    var_string = entry_text.get()
    if var_string=="":
        messagebox.showerror("Py","Input Error")
        exit(code=None)
    for widget_temp in window_nq.winfo_children():
        widget_temp.destroy()
    window_nq.destroy()
button = tk.Button(window_nq,text="finish",command=change_state).pack()
window_nq.mainloop()

#change
if plat_bool==True:
    plat_int=2
    os.chdir("C:\\Python27")
else:
    plat_int=3
    os.chdir("C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38")

#use
process_pipe = subprocess.Popen("python "+var_string,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
process_pipe.wait()
out_string = process_pipe.stdout.read().decode('gbk')
messagebox.showinfo("Return",out_string)

        
