from tkinter import *

def doSomething(event):
    # print(f"you pressed {event.keysym}")
    label.config(text=event.keysym)

window = Tk()
window.title('key events example')

# window.bind(event,function)

window.bind("<Key>", doSomething)

label = Label(window, font=("Helvetica", 100))
label.pack()

window.mainloop()