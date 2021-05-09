#import sys
from tkinter import *
import time

def times():
	current_time = time.strftime("%H:%M:%S")
	clock.config(text=current_time)
	clock.after(200,times)

root=Tk()
root.configure(background="black")
root.title("Digital Clock")
root.geometry('500x250')

digit = Label(root,text="Digital Clock",font="times 24 bold",bg='black',fg="white")
digit.grid(row=0,column=2)

clock = Label(root,font=("Algerian",50,"bold"),bg='black',fg="red")
clock.grid(row=2,column=2,pady=25,padx=100)

times()

pl = Label(root,text="     Hours       Minutes     Seconds ",font="LucidaCalligraphy 15",bg='black',fg="white")
pl.grid(row=3,column=2)

root.mainloop()