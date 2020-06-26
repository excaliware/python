#!/usr/bin/python

from sys import argv
import Tkinter
from Tkinter import *

tk = Tkinter.Tk()
frame = Tkinter.Frame(tk)
frame.pack(fill=BOTH, expand=1)

label = Tkinter.Label(frame, text=argv[1:])
label.pack(fill=X, expand=1)

button = Tkinter.Button(frame, text="Exit", command=tk.destroy)
button.pack(side=BOTTOM)

tk.mainloop()
