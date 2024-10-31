from tkinter import *
from tkinter import messagebox
import random
import json
# import pyperclip 

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*','+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("passwords.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR",message="No data file found")
    else:    
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="ERROR",message=f"No details for {website} exists.")

def generate_password():
    num_letters = random.randint(8,10)
    num_symbols = random.randint(2,4)
    num_numbers = random.randint(2,4)


    # list comprehension 
    password_letters = [random.choice(letters) for _ in range(num_letters)]
    password_symbols = [random.choice(symbols) for _ in range(num_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(num_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)


    password = "".join(password_list)
    password_entry.insert(0,password)
    # copy the password in clipboard
    # pyperclip.copy(password)
    # password = ""
    # for char in password_list:
    #     password += char
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email" : username,
            "password": password
        }
    }
    
    # entry validation and pop up for empty value
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please make sure You have not left any field empty.")
    else:
        # message box to check the entered details
# open the file in the append mode so we can create if file does not exist and update it 
        try:
            with open("passwords.json","r") as file:
                # write the data in json -> dump
                # read json data -> load
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.json","w") as file:
                json.dump(new_data,file,indent=4)
        else:
            # print(data)
            # update json data -> update
            data.update(new_data)
            with open("passwords.json","w") as data_file:
                    # load
                    json.dump(data,data_file,indent=4)
                    # clear the entry field after saving the file
        finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
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
website_entry.grid(column=1, row=1, sticky='ew')
# when the window open the cursor will be focused in this entry
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky='ew')
username_entry.insert(0,"maharshi@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='ew')  # Add sticky to expand

# Buttons
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2, row=3, sticky='ew')  # Align with password entry

add_button = Button(text="Add", width=36, command= save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='ew')

search_button = Button(text="Search",command=find_password)
search_button.grid(column=2,row=1,sticky="ew")

# Configure column weight for expansion
window.grid_columnconfigure(1, weight=1)  # Allow the first column to expand
window.grid_columnconfigure(2, weight=1)  # Allow the second column to expand

window.mainloop()