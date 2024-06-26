from tkinter import *

def add():
    listBox.insert(listBox.size(), entry.get())
    listBox.config(height=listBox.size())

def remove():
    listBox.delete(listBox.curselection())

window = Tk()
window.title("Simple To-Do List")

Label(window, text="To Do:").grid(row=0, column=0)

listBox = Listbox(window, width=30, font=("Comic Sans", 25), fg="light blue", bg="black")
listBox.grid(row=1, column=0)
listBox.insert(1,"tomae")
listBox.insert(2,"komaen")
listBox.insert(3,"tomae olet")
listBox.config(height=listBox.size()) #change height based on listbox content's size

Label(window, text="Enter your task here:").grid(row=2, column=0)

entry = Entry(window, width=30, font=("Comic Sans", 15))
entry.grid(row=3, column=0, pady=10)

frame = Frame(window, bd=2, relief=RAISED, pady=5, padx=5)
frame.grid(row=4, column=0)

addBtn = Button(frame, text="Add Task", command=add)
addBtn.grid(row=2, column=0, padx=10)

removeBtn = Button(frame, text="Remove Task", command=remove)
removeBtn.grid(row=2, column=1)



window.mainloop()