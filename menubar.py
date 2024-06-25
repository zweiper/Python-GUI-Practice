from tkinter import *

def openFile():
    print("file has been opened!")

def saveFile():
    print("file has been saved!")

def cut():
    print("you cut some text!")

def copy():
    print("you copied some text!")

def paste():
    print("you pasted some text!")

window = Tk()

menubar= Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=('Helvetica', 15))
menubar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menubar, tearoff=0, font=('Helvetica', 15))
menubar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()