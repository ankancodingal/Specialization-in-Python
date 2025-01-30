# Tkinter - 1
# 1. Import Tkinter Module
# 2. Create the GUI application main Window
# 3. Add widgets

from tkinter import *

window = Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300')

# Label
greeting = Label(text="Hello User", fg='black', bg='white')
# Button 
button = Button(text="Click me", bg='black', fg='white')
# Entry 
entry = Entry(fg="yellow", bg="blue", width=50)


greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text='Sample Frame')
label.pack()

textbox = Text(fg='green', bg='yellow')
textbox.pack()
# -----------------------------------------------------------------------------
	# Tkinter - 2
import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()


# ---------------------------------------------------------------------------
# Random Password Generator
#import the necessary modules!
import random
import string

print('hello, Welcome to Password generator!')

#input the length of password
length = int(input('\nEnter the length of password: '))             

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#string.ascii_letters

#combine the data
all = lower + upper + num + symbols

#use random 
temp = random.sample(all,length)

#create the password 
password = "".join(temp)

#print the password
print(password)
