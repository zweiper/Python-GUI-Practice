from tkinter import *

def convFahr():
    cels = float(entry.get())
    fahrenheit = (9/5 * cels) + 32
    result.config(text=str(fahrenheit))
def convCels():
    fahr = float(entry.get())
    celsius = (fahr - 32) * 5/9
    result.config(text=str(celsius))

window = Tk()
window.title("Temperature Converter")

Label(window, text="Temperature:", justify="left", font="Helvetica 15").grid(row=0, column=0)

entry = Entry(window, justify="center", font="Helvetica 15")
entry.insert(0, "0")
entry.grid(row=0, column=1, pady=5, padx=5)

Label(window, text="Result:", justify="left", font="Helvetica 15").grid(row=1, column=0)
result = Label(window, text="0", font="Helvetica 15")
result.grid(row=1, column=1)

Label(window, text="Convert To:", justify="left", font="Helvetica 15").grid(row=2, column=0)

frame = Frame(window)
frame.grid(row=2, column=1, pady=10)

btn1 = Button(frame, text="Fahrenheit", command=convFahr, width=10, font="Helvetica 12 bold", bg="#e3483d", fg="white")
btn2 = Button(frame, text="Celsius", command=convCels, width=10, font="Helvetica 12 bold", bg="#448ee3", fg="white")
btn1.grid(row=2, column=0, padx=5, pady=5)
btn2.grid(row=2, column=1, pady=5)

window.mainloop()