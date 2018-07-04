#Q1

from tkinter import*
import sys

def Display():
	print("hello world!")
	
root=Tk()
b= Button(root,text="printmsg",width=30,bg='red',fg='white',command=Display)
b.pack()
b1= Button(root,text="exit",width=30,bg='red',fg='white',command=sys.exit)
b1.pack()
root.mainloop()
	


#Q2


from tkinter import*
import sys

def Display():
	print("hello world!")
	
root=Tk()
b= Button(root,text="click",width=30,bg='red',fg='white',command=Display)
b.pack()
root.mainloop()	


#Q3
from tkinter import*
import sys

def change():
	label.config(text="how r u")
	
root=Tk()
label= Label(root,text="hello friends",width=30,bg='red',fg='white')
label.grid(row=0)
bun=Button(root,text="change",command=change)
bun.grid(row=1)
bun1=Button(root,text="exit",command=sys.exit)
bun1.grid(row=2)
root.mainloop()
	
	

#Q4	
import tkinter
from tkinter import *

def show():
	print(entry.get())
	
root=Tk()
root.title("my gui assignment")
root.geometry("350x350")
root.resizable(True,True)
root.minsize(150,150)
entry=Entry(root,width=30)
entry.pack()
b=Button(root,text='click',width=30,command=show)
b.pack()
root.mainloop()





















