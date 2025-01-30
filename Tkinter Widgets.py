# Image makes it better!
# Make sure you upload image in your current Repl
# Import all the necessary libraries
# PIL (Python Imaging Library) provides image editing capabilities to the python interpreter 
from tkinter import *
from PIL import Image, ImageTk

# Create a window with a title bar and set its geometry as well
root = Tk()
root.title('image')
root.geometry('400x400')

# Now use Image.open to open and identify the given image file. 
upload = Image.open("img.jpg")

# Convert this Image to Tkinter compatible image
image = ImageTk.PhotoImage(upload)

# Add image to Tkinter Label
label = Label(root, image=image, height=350, width=300)
label.place(x=50, y=0)
label2 = Label(root, text="This is how you add image in Tkinter Window")
label2.place(x=40, y=360)

# Run the application
root.mainloop()

# ---------------------------------------------------------------------------------------------
# Alert! Virus Detected
# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.geometry("200x200")

# Function for Displaying Warning Message
# This will be called once the button is clicked
# messagebox.showwarning("Window Name", "Text to be displayed")
def msg():
	messagebox.showwarning("Alert", "Stop! Virus Found.")

# Adding Button Widget to Window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

# Entering main event loop
root.mainloop()
# ----------------------------------------------------------------------------------
# Let's Top a Window
# Import necessary libraries
from tkinter import *
 
# Setting up Main Window
root = Tk()
root.geometry("400x300")
root.title("main")

# Function to open New (Top Level) Window
def topwin():
	# Setting up Top Window
	top = Toplevel()
	top.geometry("180x100")
	top.title("toplevel")
	# Adding a label widget to Top Window
	l2 = Label(top, text = "This is toplevel window")
	l2.pack()

	top.mainloop()

# Adding a label and button Widget to Root (Main) Window
l = Label(root, text = "This is root window")
btn = Button(root, text = "Click here to open another window", command = topwin)

# Arranging widgets
l.pack()
btn.pack()


# ----------------------------------------------------------------------------------------
# Rock, Paper, Scissor
import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')
while (1 < 2):
    print('\n')
    print("Rock, Paper, Scissors - Shoot!")
    userChoice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
    if not re.match("[SsRrPp]", userChoice):
        print("Please choose a letter:")
        print("[R]ock, [S]cissors or [P]aper.")
        continue
    # Echo the user's choice
    print("You chose: " + userChoice)
    choices = ['R', 'P', 'S']
    opponenetChoice = random.choice(choices)
    print("I chose: " + opponenetChoice)
    if opponenetChoice == str.upper(userChoice):
        print("Tie! ")
    #if opponenetChoice == str("R") and str.upper(userChoice) == "P"
    elif opponenetChoice == 'R' and userChoice.upper() == 'S':      
        print("Scissors beats rock, I win! ")
        continue
    elif opponenetChoice == 'S' and userChoice.upper() == 'P':      
        print("Scissors beats paper! I win! ")
        continue
    elif opponenetChoice == 'P' and userChoice.upper() == 'R':      
        print("Paper beat rock, I win! ")
        continue
    else:       
        print("You win!")
