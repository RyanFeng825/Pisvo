import time as t
from tkinter import messagebox
import win32api, win32gui

def read():
    global list_read
    list_read = []
    try:
        q=open("num.txt","r+")
    except:
        q=open("num.txt","w+")
        q.close()
        q=open("num.txt","r+")
    for line in q.readlines():
        list_read.append(int(line))

def most_frequent():
    read()
    try:
        return max(set(list_read), key = list_read.count)
    except:
        return ""

def main():
    most = most_frequent()
    while 1:
        try:
            sub=raw_input("Please the time in second and an int["+str(most)+"]:")
            if sub==""and most!="":
                sub=int(most)
            elif sub=="" and most=="":
                messagebox.showinfo("Error","Input Error")
                continue
            else:
                q=open("num.txt","a+")
                q.write(sub+"\n")
                q.close()
                sub=int(sub)
            break
        except:
            messagebox.showinfo("Error","Input Error")
            continue
    ct = win32api.GetConsoleTitle()
    hd = win32gui.FindWindow(0,ct)
    win32gui.ShowWindow(hd,0)
    while True:
        now=t.time()
        while 1:
            sub_check=t.time()-now
            if sub_check>=sub:
                messagebox.showinfo("Tips","The time you set is up.Please rest!")
                break
            
main()
    
