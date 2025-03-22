from tkinter import * 

window = Tk()

window.title("Thinker GUI")
window.geometry("600x400")

# Label 
label = Label(window, text="Hello, World!")
label.place(x= 20, y= 100)

# Entry
entry = Entry(window, text = "Enter your name")
entry.place(x= 200, y= 100)
def show():    
    print(entry.get())

# Font Style
from tkinter import font
buttonfont = font.Font(family='Times New Romain', size= 8, weight='bold')

# Button and command
button = Button(window, text="Click Me!" ,font = buttonfont,height= 2,width=8, command= show)
button.place(x= 400, y= 100)
    # With pack funtion
    # btn.pack(side=RIGHT, padx=15, pady=20)

# Checkbutton
checkbutton = Checkbutton(window, text="Remember me")
checkbutton.place(x= 200, y= 150)

# Radiobutton
radio = Radiobutton(window, text = "Radioutton 1", value= 1)
radio.place(x= 200, y= 200)

# Listbox
listbox = Listbox(window)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.insert(4, "C#")
listbox.place(x= 200, y= 250)

# Spinbox
spinbox = Spinbox(window, from_=0, to=100)
spinbox.place(x= 200, y= 300)

# Scale
scale = Scale(window, from_=0, to=100, orient=HORIZONTAL)
scale.place(x= 200, y= 350)

# Text
text = Text(window, height= 5, width= 20)
text.place(x= 400, y= 200)

# Message
message = Message(window, text="This is a message")
message.place(x= 400, y= 300)

# Menu
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit")

# Frame
frame = Frame(window, width= 200, height= 200)
frame.place(x= 100, y= 100)
frame.pack_propagate(0)
frame.pack()

# Canvas
canvas = Canvas(window, width= 200, height= 200)
canvas.place(x= 100, y= 100)
canvas.create_line(0, 0, 200, 100)
canvas.create_rectangle(50, 25, 150, 75, fill="blue")

# Scrollbar
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(window, xscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT)
scrollbar.config(command=listbox.yview)

# Progressbar
from tkinter.ttk import Progressbar
progressbar = Progressbar(window, length= 200, mode='determinate')
progressbar.place(x= 200, y= 100)
progressbar.start()

# LabelFrame
labelframe = LabelFrame(window, text="This is a LabelFrame")
labelframe.place(x= 200, y= 200)
label = Label(labelframe, text="Hello, World!")
label.pack()

# PanedWindow
panedwindow = PanedWindow(window)
panedwindow.pack(fill=BOTH, expand=1)
left = Entry(panedwindow, bd=5)
panedwindow.add(left)

panedwindow = PanedWindow(panedwindow, orient=VERTICAL)
panedwindow.pack(fill=BOTH, expand=1)
top = Scale(panedwindow, orient=HORIZONTAL)
panedwindow.add(top)

bottom = Button(panedwindow, text="OK")
panedwindow.add(bottom)

'''
# MessageBox
from tkinter import messagebox
messagebox.showinfo("Information", "Information Message")
messagebox.showerror("Error", "Error Message")
messagebox.showwarning("Warning", "Warning Message")


# Color Chooser
from tkinter.colorchooser import askcolor
color = askcolor()
print(color)

# File Dialog
from tkinter.filedialog import askopenfilename
filename = askopenfilename()
print(filename)

# Directory Dialog
from tkinter.filedialog import askdirectory
directory = askdirectory()
print(directory)


# Font Chooser
from tkinter.filedialog import askfont
font = askfont()
print(font)
'''

# Dialog
from tkinter.simpledialog import askstring
string = askstring("Input", "Enter your name")
print(string)

from tkinter.simpledialog import askinteger
integer = askinteger("Input", "Enter your age")
print(integer)

from tkinter.simpledialog import askfloat
float = askfloat("Input", "Enter your weight")
print(float)

# Dialog
from tkinter.simpledialog import Dialog
class MyDialog(Dialog):
    def body(self, master):
        Label(master, text="First:").grid(row=0)
        Label(master, text="Second:").grid(row=1)
        self.e1 = Entry(master)
        self.e2 = Entry(master)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1

    def apply(self):
        first = self.e1.get()
        second = self.e2.get()
        print(first, second)

MyDialog(window, title="My Dialog")

# Treeview
from tkinter import ttk
tree = ttk.Treeview(window)
tree["columns"] = ("one", "two")
tree.column("one", width=100)
tree.column("two", width=100)
tree.heading("one", text="column A")
tree.heading("two", text="column B")
tree.insert("", END, text="line 1", values=("A1", "B1"))
tree.insert("", END, text="line 2", values=("A2", "B2"))
tree.pack()

# Notebook
from tkinter import ttk
notebook = ttk.Notebook(window)
notebook.pack()
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text="One")
notebook.add(frame2, text="Two")

#combobox
from tkinter import ttk
combo = ttk.Combobox(window)
combo["values"] = ("A", "B", "C")
combo.pack()


# Main Loop
window.mainloop()