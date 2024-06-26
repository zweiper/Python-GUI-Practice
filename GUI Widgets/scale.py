from tkinter import *

def submit():
    print(f"Temperature is {str(scale.get())} degrees C")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font = ("Arial", 20),
              tickinterval=10, #shows numbers beside the scale
              showvalue=0, #hides current value
              fg="#00FF00",
              bg="black",
              troughcolor="#00FF00" #color for scrollbar
              )
scale.set(50)
scale.pack()

button = Button(window, text="submit", command=submit)
button.pack()


window.mainloop()
