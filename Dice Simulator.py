import random
from tkinter import *

root=Tk()
root.geometry("700x450")

#GUI componets
#1st parameter is the GUI instance then the text and then the font
l1=Label(root,font=("times",200))

def roll():
    #all ascii characters of the numbers
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}')
    l1.pack()

#button
b1=Button(root,text="lets roll",command=roll,activebackground="yellow",background="blue")
#we want to palce the button at the middle horizontally and at the top
b1.place(x=350,y=0)

root.mainloop()
