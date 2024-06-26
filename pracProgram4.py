from tkinter import *
from tkinter import messagebox

def login():
    uname = username.get()
    pname = password.get()
    output = "Username: " + uname + "\nPassword: " + pname
    messagebox.showinfo(title="Login Successful!", message=output)

window = Tk()
window.title("Login Form")

Label(window, text="Username:", font=("Arial", 15)).grid(row=0, column=0)
Label(window, text="Password:", font=("Arial", 15)).grid(row=1, column=0)

username = Entry(window, font=("Arial", 15))
password = Entry(window, show="*", font=("Arial", 15))
username.grid(row=0, column=1, pady=8)
password.grid(row=1, column=1)

login = Button(window, text="Login", command=login, font=("Arial", 15), width=10, fg="#00FF00", bg="black", activeforeground="#00FF00", activebackground="black")
login.grid(row=3, column=1, pady=8)

window.mainloop()