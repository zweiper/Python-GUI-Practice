from tkinter import *

window = Tk() #instantiate an instance of window
window.geometry('500x500')
window.title('Python GUI')

icon = PhotoImage(file='sakuya.png')
window.iconphoto(True, icon)

window.config(background='#00aaff')

window.mainloop()