#!/usr/bin/env python3

import tkinter as tk
import expressiontree


def printtree():
    try:
        expression = inputbox.get()
        tmpout = expressiontree.printdata(expression)
        outputbox.configure(state='normal')
        outputbox.delete("1.0", tk.END)
        outputbox.insert(tk.END, ('\n' + tmpout))
        outputbox.configure(state='disabled')
    except:
        outputbox.configure(state='normal')
        outputbox.delete("1.0", tk.END)
        outputbox.insert(tk.END, '\nThe expression entered caused some problems.')
        outputbox.configure(state='disabled')

def about():
    outputbox.configure(state='normal')
    outputbox.delete("1.0", tk.END)
    outputbox.insert(tk.END, '\nVisit https://github.com/Dual-Exhaust/expressiontree for more information.')
    outputbox.configure(state='disabled')
window = tk.Tk()

enterlabel = tk.Label(text="Enter Infix Expresssion")
inputbox = tk.Entry(width=25)
outputbox = tk.Text()

enterbutton = tk.Button(
    text="Enter",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=printtree
)

aboutbutton = tk.Button(
    text="About",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=about
)

enterlabel.pack()
inputbox.pack()
enterbutton.pack()
aboutbutton.pack()
outputbox.pack()
window.mainloop()
