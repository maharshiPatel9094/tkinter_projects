from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

# image canvas 
canvas = Canvas(height=200,width=200)
logo_image = PhotoImage(file="./logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.pack()



window.mainloop()