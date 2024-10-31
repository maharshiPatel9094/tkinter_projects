from tkinter import *
import pandas
import random

# constants
BACKGROUND_COLOR = "#B1DDC6"



# CSV data to list of dict
data = pandas.read_csv("./data/french_words.csv")
# setting orient to records it makes a list of dictionaries
# so we can pick any random value from list and acces the french and english value
words_data = data.to_dict(orient="records")
# print(data)

current_card = {}

# functions
def next_card():
    global current_card,flip_timer
    current_card = random.choice(words_data)
    canvas.itemconfig(canvas_title,text="French",fill="black")
    canvas.itemconfig(canvas_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    # current_card["English"]
    # flip the card after 3 sec
    window.after(3000,func = flip_card)

def flip_card():
    canvas.itemconfig(canvas_title,text="English",fill="white")
    canvas.itemconfig(canvas_word,text=current_card["English"],fill="white")
    # we can not create photoimage inside the function because once the function gets runned it will lost his reference
    canvas.itemconfig(card_background,image=card_back_img)


# window setup
window = Tk()
window.title("FLASH CARD PROJECT")
# padding and bg color set
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)


flip_timer = window.after(3000,func=flip_card)

# canvas setup
# to remove the white line from the canvas we use highlightthickness = 0
canvas = Canvas(height=526,width=800,highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400,263,image=card_front_img)
card_back_img = PhotoImage(file="./images/card_back.png")

# here in the text the position of x and y is respect to the canvas
canvas_title = canvas.create_text(400,150,text="Title",font=("Arial",60,"bold"))
canvas_word = canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"))
# to remove the background color of canvas
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0,row=0,columnspan=2,sticky="nsew")

# buttons 
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image,highlightthickness=0,command=next_card)
right_button.grid(column=1,row=1)
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)


# calling the next card function so it does not show us the initial card phase 
# so as soon as we run we will see the french word and not the title and word 
next_card()

# window control
window.mainloop()