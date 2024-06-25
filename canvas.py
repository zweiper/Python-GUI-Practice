from tkinter import *

window = Tk()
window.title("Canvas Example")

canvas = Canvas(window, width=500, height=500)
# canvas.create_line(0,0,500,500,fill="blue",width=5)
# canvas.create_line(0,500,500,0,fill="red",width=5)
# canvas.create_rectangle(50,50,250,250,fill="purple")
# points = [250,0,500,500,0,500]
# canvas.create_polygon(points, fill="yellow",outline="black",width=5)

canvas.pack()
window.mainloop()