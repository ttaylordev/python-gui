import tkinter as tk
from tkinter import filedialog, Text
from tkinter import *
import os

# assign tk as the root of the project
root = tk.Tk()
apps = []

# define functions for buttons
def addApp():
    filename= filedialog.askopenfile(initialdir='/', title="Select File",
        filetypes=(('executables', '*.exe'), ('all files', '*.*')))
    apps.append(filename)
    print(filename)
    
# def runApp():

# create a canvas
canvas = tk.Canvas(root, height=720, width=720, bg="#424242")


# attach it to the root
canvas.pack()

# inner frame
frame = tk.Frame(root, bg='white')
# attach it to the root and provide some 
# padding & center it within the canvas
frame.place(relwidth=0.975, relheight=0.975, relx=0.0125, rely=0.0125)

# add some buttons
openFile = tk.Button(root, text='Open File', padx=10, 
                        pady=5, fg='white', bg='#424242', command=addApp)
openFile.pack()

runApps = tk.Button(root, text='Run Aapps', padx=10, pady=5, 
                        fg='white', bg='#424242')
runApps.pack()

# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )

# redbutton = Button(frame, text="Red", fg="red")
# redbutton.pack( side = LEFT)

# greenbutton = Button(frame, text="green", fg="green")
# greenbutton.pack( side = LEFT )

# bluebutton = Button(frame, text="Blue", fg="blue")
# bluebutton.pack( side = LEFT )

# blackbutton = Button(bottomframe, text="Black", fg="black")
# blackbutton.pack( side = BOTTOM)


root.mainloop()
