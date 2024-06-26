from tkinter import *

count = 0
def click():
    global count
    print("You clicked the button!")
    count+=1
    print(count)

window = Tk()

button = Button(window,
                text='Click me!',
                command=click,
                font=('Comic Sans', 30),
                fg="#00FF00",
                bg='black',
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE)
button.pack()
window.mainloop()