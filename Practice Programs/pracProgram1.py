from tkinter import *

class Functions:
    def __init__(self, entry1, entry2):
        self.entry1 = entry1
        self.entry2 = entry2

    def get_numbers(self):
        self.num1 = float(self.entry1.get())
        self.num2 = float(self.entry2.get())
    def add(self):
        self.get_numbers()
        ans_sum = self.num1 + self.num2
        print(f"{self.num1} + {self.num2} = {ans_sum}")

    def minus(self):
        self.get_numbers()
        diff = self.num1 - self.num2
        print(f"{self.num1} + {self.num2} = {diff}")

    def multiply(self):
        self.get_numbers()
        prod = self.num1 * self.num2
        print(f"{self.num1} * {self.num2} = {prod}")

    def divide(self):
        self.get_numbers()
        quo = self.num1 / self.num2
        print(f"{self.num1} / {self.num2} = {quo}")

window = Tk()
window.title("Simple Calculator")
window.geometry("500x300")

label1 = Label(window, text="Enter 1st Number:")
label1.grid(row=0, column=0, )

entry1 = Entry(window, font=("Helvetica", 20))
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = Label(window, text="Enter 2nd Number:", pady=10)
label2.grid(row=1, column=0)

entry2 = Entry(window, font=("Helvetica", 20))
entry2.grid(row=1, column=1, padx=10, pady=10)

frame = Frame(window, width=300, height=200, bd=5, relief="sunken")
frame.grid(row=3, column=1)

functions = Functions(entry1, entry2)
Button(frame, text="+", command=functions.add, height=5, width=8).grid(row=1, column=1)
Button(frame, text="-", command=functions.minus, height=5, width=8).grid(row=3, column=0)
Button(frame, text="x", command=functions.multiply, height=5, width=8).grid(row=3, column=1)
Button(frame, text="/", command=functions.divide, height=5, width=8).grid(row=3, column=2)


window.mainloop()