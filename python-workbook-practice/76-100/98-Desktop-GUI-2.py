# Create a Desktop app, that takes an input text and has 3 click-buttons - Add File, Save File, Save and Close 
# Use Tkinter module

import tkinter
from tkinter import *

# window is the container in Tkinter that stores all other GUI elements
# window is an instance of Tkinter's Tk class

# create a new window and assign it to the window variable

window=tkinter.Tk()
window.title('First GUI app')

frame=tkinter.Frame(window)
frame.pack()

# We use button widgets to add a clickable-buttons

button=tkinter.Button(frame, text='Add File')
button.pack()

button1=tkinter.Button(frame, text='Save File')
button1.pack()

button2=tkinter.Button(frame, text='Save and Close')
button2.pack()

# Get User Inputs with Entry Widgets

entry=tkinter.Entry(width=50)

# You need to .pack() the widgets into the window so that they’re visible

entry.pack()

## Now use .get() on entry to assign the user input to a variable

user_input = entry.get()

window.mainloop()           # This is the MOST IMPORTANT method to run the GUI app 

# The above opens a pop-up window -- WORKS GREAT #####


#F1=Frame(window, height=50, width=50)
#F1.pack()


# dir(tkinter)

# ['ACTIVE', 'ALL', 'ANCHOR', 'ARC', 'BASELINE', 'BEVEL', 'BOTH', 'BOTTOM', 'BROWSE', 'BUTT', 'BaseWidget', 'BitmapImage', 
# 'BooleanVar', 'Button', 'CASCADE', 'CENTER', 'CHAR', 'CHECKBUTTON', 'CHORD', 'COMMAND', 'CURRENT', 'CallWrapper', 'Canvas', 
# 'Checkbutton', 'DISABLED', 'DOTBOX', 'DoubleVar', 'E', 'END', 'EW', 'EXCEPTION', 'EXTENDED', 'Entry', 'Event', 'EventType', 
# 'FALSE', 'FIRST', 'FLAT', 'Frame', 'GROOVE', 'Grid', 'HIDDEN', 'HORIZONTAL', 'INSERT', 'INSIDE', 'Image', 'IntVar', 'LAST', 
# 'LEFT', 'Label', 'LabelFrame', 'Listbox', 'MITER', 'MOVETO', 'MULTIPLE', 'Menu', 'Menubutton', 'Message', 'Misc', 'N', 'NE', 
# 'NO', 'NONE', 'NORMAL', 'NS', 'NSEW', 'NUMERIC', 'NW', 'NoDefaultRoot', 'OFF', 'ON', 'OUTSIDE', 'OptionMenu', 'PAGES', 
# 'PIESLICE', 'PROJECTING', 'Pack', 'PanedWindow', 'PhotoImage', 'Place', 'RADIOBUTTON', 'RAISED', 'READABLE', 'RIDGE', 
# 'RIGHT', 'ROUND', 'Radiobutton', 'S', 'SCROLL', 'SE', 'SEL', 'SEL_FIRST', 'SEL_LAST', 'SEPARATOR', 'SINGLE', 'SOLID', 
# 'SUNKEN', 'SW', 'Scale', 'Scrollbar', 'Spinbox', 'StringVar', 'TOP', 'TRUE', 'Tcl', 'TclError', 'TclVersion', 'Text', 'Tk', 
# 'TkVersion', 'Toplevel', 'UNDERLINE', 'UNITS', 'VERTICAL', 'Variable', 'W', 'WORD', 'WRITABLE', 'Widget', 'Wm', 'X', 'XView', 
# 'Y', 'YES', 'YView', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__',
#  '__spec__', '_cnfmerge', '_default_root', '_exit', '_flatten', '_join', '_magic_re', '_setit', '_space_re', '_splitdict', 
# '_stringify', '_support_default_root', '_test', '_tkerror', '_tkinter', '_varnum', 'constants', 'enum', 'getboolean', 
# 'getdouble', 'getint', 'image_names', 'image_types', 'mainloop', 're', 'sys', 'wantobjects']
