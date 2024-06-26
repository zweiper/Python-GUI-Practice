from tkinter import *


def create_window():
    # new_window = Toplevel() #creates a new window on top of the existing window
    new_window = Tk() #creates an independent window
    old_window.destroy() #destroys the old window

old_window = Tk()
old_window.title('New Window in GUI Python')

Button(old_window, text="Create New Window", command=create_window).pack()


old_window.mainloop()