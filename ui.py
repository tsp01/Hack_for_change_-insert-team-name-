"""
This file is for generating UI
"""
from tkinter import *
from tkinter import ttk

class Ui:
    def __init__(self):
        pass

    def display_current_groceries():
        pass

    def display_notification():
        pass

    def food_adder():
        pass




root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()