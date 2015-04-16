import sys
from tkinter import *
from tkinter import ttk
from login import *



root = Tk()
root.configure(background='firebrick2', padx=20, pady=20)
root.geometry('1000x600+10+10')

window_width = 600
window_height = 600


login_frame = Frame(root, bg='firebrick2')

login_frame.pack()

login = Login(login_frame, root)





root.mainloop()