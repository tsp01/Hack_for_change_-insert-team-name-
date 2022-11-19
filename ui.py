"""
This file is for generating UI
"""
from tkinter import *
from tkinter import ttk

class Ui:
    def __init__(self):
        
        pass

    def display_main(self):
        pass

    def display_current_groceries(self):
        pass

    def display_notification(self, food, count):
        pass

    def food_adder(self):
        pass

root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Button(frm, text="Add Product").grid(column=0, row=0)
e = ttk.Entry(frm, cursor = 'xterm').grid(column=1, row=0)
root.mainloop()