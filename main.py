from tkinter import *
from ieee754 import *
def goo():
    num=num_entry.get()
    num_entry.delete(0,END)
    num_entry.insert(0,IEEE754(num))

window=Tk()

window.title("IEEE754")
window.geometry("1080x720")
window.minsize(480,360)
window.iconbitmap("icon.ico")
window.config(background="black")

frame=Frame(window,bg="black")
title_label=Label(frame,text="IEEE754",bg="black",font=("Ubuntu",40),fg="white")
title_label.pack()
num_entry=Entry(frame,bg="black",font=("Ubuntu",20),fg="white",width=33)
num_entry.pack(fill=X)
genarate=Button(frame,bg="black",text="go",font=("Ubuntu",40),fg="white",command=goo)
genarate.pack()
frame.pack(expand=YES)

window.mainloop()

