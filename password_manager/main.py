from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Image canvas
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="./logo.png")  # Ensure the path is correct
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry fields
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky='ew')

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky='ew')

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='ew')  # Add sticky to expand

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky='ew')  # Align with password entry

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky='ew')

# Configure column weight for expansion
window.grid_columnconfigure(1, weight=1)  # Allow the first column to expand
window.grid_columnconfigure(2, weight=1)  # Allow the second column to expand

window.mainloop()
