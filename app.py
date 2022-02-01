import tkinter as tk
from tkinter import filedialog, Text
# from tkinter import *
import os

# assign tk as the root of the project
root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps  = f.read()
        tempApps = tempApps.split(',')
        print(tempApps)
        apps = [x for x in tempApps if x.strip()]

# define functions for buttons
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir='/', title="Select File", filetypes=(('executables', '*.exe'), ('all files', '*.*')))
    apps.append(filename)
    print(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg='grey')
        label.pack()

def runApp():
    for app in apps:
        os.startfile(app)

# create a canvas
canvas = tk.Canvas(root, height=720, width=720, bg="#424242")
# attach it to the root
canvas.pack()

# inner frame
frame = tk.Frame(root, bg='white')
# attach it to the root and provide some borders & center it within the canvas
frame.place(relwidth=0.975, relheight=0.975, relx=0.0125, rely=0.0125)

# add some buttons
openFile = tk.Button(root, text='Open File', padx=10, pady=5, fg='white', bg='#424242', command=addApp)
openFile.pack()

runApps = tk.Button(root, text='Run Aapps', padx=10, pady=5, fg='white', bg='#424242', command=runApp)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
            f.write(app + ',')
        # f.write(app + ',\n')



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
