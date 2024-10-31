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


# functions
def next_card():
    current_card = random.choice(words_data)
    canvas.itemconfig(canvas_title,text="French")
    canvas.itemconfig(canvas_word,text=current_card["French"])
    # current_card["English"]


# window setup
window = Tk()
window.title("FLASH CARD PROJECT")
# padding and bg color set
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)


# canvas setup
# to remove the white line from the canvas we use highlightthickness = 0
canvas = Canvas(height=526,width=800,highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400,263,image=card_front_img)
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
next_card()

# window control
window.mainloop()