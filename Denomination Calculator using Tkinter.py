# Denomination Calculator using Tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload = Image.open("app_img.jpg")
# Resize the image using resize() method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root,
               text="Hey User! Welcome to Denomination Counter Application.",
               bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

# Adding Buttons to the main window
button1 = Button(root,
                 text="Let's get started!",
                 command=msg,
                 bg='brown',
                 fg='white')
button1.place(x=260, y=360)

# Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")
    

    label = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey')

    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white')

    # Centering Widgets in the Top Window
    label.place(x=230, y=50   )
    entry.place(x=200, y=80   )
    btn.place(x=240, y=120   )
    lbl.place(x=140, y=170   )

    l1.place(x=180, y=200   )
    l2.place(x=180, y=230   )
    l3.place(x=180, y=260   )

    t1.place(x=270, y=200   )
    t2.place(x=270, y=230   )
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()
# -------------------------------------------------------------------------------------------
	# Rock, Paper, Scissor GUI
# Import Required Library
from tkinter import *
import random

# Create Object
root = Tk()

# Set geometry
root.geometry("300x300")

# Set title
root.title("Rock Paper Scissor Game")
root.attributes('-fullscreen', True)

# Computer Value
computer_value = {
	"0":"Rock",
	"1":"Paper",
	"2":"Scissor"
}

# Reset The Game
def reset_game():
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	l1.config(text = "Player			 ")
	l3.config(text = "Computer")
	l4.config(text = "")

# Disable the Button
def button_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"

# If player selected rock
def isrock():
	c_v = computer_value[str(random.randint(0,2))]
	if c_v == "Rock":
		match_result = "Match Draw"
	elif c_v=="Scissor":
		match_result = "Player Win"
	else:
		match_result = "Computer Win"
	l4.config(text = match_result)
	l1.config(text = "Rock		 ")
	l3.config(text = c_v)
	button_disable()

# If player selected paper
def ispaper():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Paper":
		match_result = "Match Draw"
	elif c_v=="Scissor":
		match_result = "Computer Win"
	else:
		match_result = "Player Win"
	l4.config(text = match_result)
	l1.config(text = "Paper		 ")
	l3.config(text = c_v)
	button_disable()

# If player selected scissor
def isscissor():
	c_v = computer_value[str(random.randint(0,2))]
	if c_v == "Rock":
		match_result = "Computer Win"
	elif c_v == "Scissor":
		match_result = "Match Draw"
	else:
		match_result = "Player Win"
	l4.config(text = match_result)
	l1.config(text = "Scissor		 ")
	l3.config(text = c_v)
	button_disable()

# Add Labels, Frames and Button
Label(root,
	text = "Rock Paper Scissor",
	font = "normal 20 bold",
	fg = "blue").pack(pady = 20)

frame = Frame(root)
frame.pack()

l1 = Label(frame,
		text = "Player			 ",
		font = 10)

l2 = Label(frame,
		text = "VS			 ",
		font = "normal 10 bold")

l3 = Label(frame, text = "Computer", font = 10)

l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()

l4 = Label(root,
		text = "",
		font = "normal 20 bold",
		bg = "white",
		width = 15 ,
		borderwidth = 2,
		relief = "solid")
l4.pack(pady = 20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text = "Rock",
			font = 10, width = 7,
			command = isrock)

b2 = Button(frame1, text = "Paper ",
			font = 10, width = 7,
			command = ispaper)

b3 = Button(frame1, text = "Scissor",
			font = 10, width = 7,
			command = isscissor)

b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(padx = 10)

Button(root, text = "Reset Game",
	font = 10, fg = "red",
	bg = "black", command = reset_game).pack(pady = 20)

# Excecute Tkinter
root.mainloop()
