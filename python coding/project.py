from tkinter import *
import datetime
from PIL import ImageTk, Image
import random

def clear():
    counter = 0
    if CheckVar1.get() == 1:
        counter += 1
    if CheckVar2.get() == 1:
        counter += 1
    if CheckVar3.get() == 1:
        counter += 1
    if CheckVar4.get() == 1:
        counter += 1
    if CheckVar5.get() == 1:
        counter += 1
    if CheckVar6.get() == 1:
        counter += 1
    print(int(counter))
    f = open("cats.txt", "a")
    f.write(str(counter))
    f.write("\n")
    f.close()
    CheckVar1.set(0)
    CheckVar2.set(0)
    CheckVar3.set(0)
    CheckVar4.set(0)
    CheckVar5.set(0)
    CheckVar6.set(0)
    counter = 0

def open1():
    f = open("cats.txt", "r")
    print(f.read())

#def change():

    #print("yes")

    #img2 = ImageTk.PhotoImage(Image.open("cat2.jpg"))
    #myimage.config(myimage = img2) 
    #myimage.photo_ref = img2

    #img1 = "cat2.jpg" 
    
win = Tk()
win.title("reminders")
win.geometry("500x500")
win.configure(background='lightgrey')

CheckVar1=IntVar()
CheckVar2=IntVar()
CheckVar3=IntVar()
CheckVar4=IntVar()
CheckVar5=IntVar()
CheckVar6=IntVar()

x = datetime.datetime.now()
l1 = Label(win, text = (x.strftime("%B"),x.strftime("%d")),anchor='nw')
l1.place(x = 0, y = 0)
l1.config(font=("Courier", 30))

x = datetime.datetime.now()
l2 = Label(win, text = (x.strftime("%I"),":",x.strftime("%M")))
l2.place(x = 363, y = 0)
l2.config(font=("Courier", 30))

canvas = Canvas(win,height=300,width=480)
canvas.place(x = 10, y= 50)

img1 = "cat1.jpg"
image = img1
myimage = Image.open(image)
myimage = myimage.resize((480, 300), Image.ANTIALIAS)
myimg = ImageTk.PhotoImage(myimage)
canvas.create_image(0, 0, image=myimg,anchor= 'nw')    

c1 = Checkbutton(win, text = "Fill water",variable = CheckVar1,onvalue = 1, offvalue = 0)
c1.place(x = 100, y = 360)
c2 = Checkbutton(win, text = "Fill water",variable = CheckVar2,onvalue = 1, offvalue = 0)
c2.place(x = 100, y = 385)
c3 = Checkbutton(win, text = "Fill water",variable = CheckVar3,onvalue = 1, offvalue = 0)
c3.place(x = 100, y = 410)

c4 = Checkbutton(win, text = "Fill food",variable = CheckVar4,onvalue = 1, offvalue = 0)
c4.place(x = 300, y = 360)
c5 = Checkbutton(win, text = "Fill food",variable = CheckVar5,onvalue = 1, offvalue = 0)
c5.place(x = 300, y = 385)
c6 = Checkbutton(win, text = "Scoop Litter",variable = CheckVar6,onvalue = 1, offvalue = 0)
c6.place(x = 300, y = 410)

b3 = Button(win, text = "file", command = open1)
b3.place(x = 40, y = 450)
b3.config(font=("Courier", 30),relief=SUNKEN)

b2 = Button(win, text = "reset", command = clear)
b2.place(x = 195, y = 450)
b2.config(font=("Courier", 30),relief=SUNKEN)

#b4 = Button(win, text = "change", command = change)
#b4.place(x = 265, y = 450)
#b4.config(font=("Courier", 30),relief=SUNKEN)

b1 = Button(win, text = "quit", command = quit)
b1.place(x = 380, y = 450)
b1.config(font=("Courier", 30),relief=SUNKEN)

mainloop()
