# create a web app, which asks user to enter a string or a word as an input in the GUI.
# Once the input is entered, it should write a file webapp.txt to the local workspace
# 

import flask
import tkinter

from flask import *
from tkinter import Tk

app=Flask(__name__)

@app.route('/')

def home():
    window=tkinter.Tk()
    #file = open("webapp.txt", "a+")

    #user_value = StrVar()
    #user_value = input('')
    entry = Entry(window, textvariable=user_value)
    entry.grid(row=0, column=0)
 
    button_add = Button(window, text="Add line")
    button_add.grid(row=0, column=1)

    #def add():
    #    file.write(user_value.get() + "\n")
    #    entry.delete(0, END)
    #    file.close()
    #    file = open("user_gui.txt", "a+")
    
    window.mainloop()
    
    return 'success'

