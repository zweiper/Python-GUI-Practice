from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title="This is an info message box", message = "You are a person")
    # messagebox.showwarning(title="WARNING!", message="YOU HAVE A VIRUS!!!")
    # messagebox.showerror(title="ERROR!", message="something went wrong...")
    # if messagebox.askokcancel(title="ask ok cancel", message="Do you want to do the thing?"):
    #     print("you did a thing!")
    # else:
    #     print("you canceled a thing! :c")
    # if messagebox.askretrycancel(title="ask retry cancel", message="Do you want to retry the thing?"):
    #     print("you retried the thing!")
    # else:
    #     print("you canceled a thing! :c")
    # if messagebox.askyesno(title="ask yes no", message="Do you like cake?"):
    #     print("I like cake, too! c:")
    # else:
    #     print("Why don't you like cake? :c")
    # answer = messagebox.askquestion('Ask question', 'Do you like pie?')
    # if answer == 'yes':
    #     print("I like pie too! c:")
    # else:
    #     print("Why don't you like pie? :c")
    print(messagebox.askyesnocancel('yes no cancel', 'Do you like to code?'))

window = Tk()


button = Button(window, command=click, text="Click Me!")
button.pack()

window = mainloop()