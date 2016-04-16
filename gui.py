from tkinter import *
import random

root = Tk()
root.title("Hello World!")
root.geometry('300x200')

colors = ["white","yellow","pink", "green","black"]

def button_clicked(num):
    print("Hello "+str(num))
    print(button1['text'],button2['text'],button3['text'])


def b1():
    button_clicked(1)
    # button1['text']='2'
    # button1['bg']="green"

def b2():
    button_clicked(2)

def b3():
    button_clicked(3)

def close():
    root.destroy()
    root.quit()

button1 = Button(root, text=colors[random.randrange(0,5)], command=b1)
button2 = Button(root, text=colors[random.randrange(0,5)], command=b2)
button3 = Button(root, text=colors[random.randrange(0,5)], command=b3)
button1.pack(fill=BOTH)
button2.pack(fill=BOTH)
button3.pack(fill=BOTH)

root.protocol('WM_DELETE_WINDOW', close)

root.mainloop()