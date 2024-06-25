from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

window = Tk()

x = IntVar()

for index in range (len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],
                               variable=x,
                               value=index)
    radio_button.pack()

window.mainloop()