from tkinter import *
import pandas
import random

# constants
BACKGROUND_COLOR = "#B1DDC6"


current_card = {}
words_data = {}
# CSV data to list of dict
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    words_data = data.to_dict(orient="records")
else:
# setting orient to records it makes a list of dictionaries
# so we can pick any random value from list and acces the french and english value
    words_data = data.to_dict(orient="records")
# print(data)





# card will only flip when you are on a new card for a 3 sec otherwise it wont flip

# functions
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_data)
    canvas.itemconfig(canvas_title,text="French",fill="black")
    canvas.itemconfig(canvas_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    # current_card["English"]
    # flip the card after 3 sec
    flip_timer = window.after(3000,func = flip_card)

def flip_card():
    canvas.itemconfig(canvas_title,text="English",fill="white")
    canvas.itemconfig(canvas_word,text=current_card["English"],fill="white")
    # we can not create photoimage inside the function because once the function gets runned it will lost his reference
    canvas.itemconfig(card_background,image=card_back_img)

def is_known():
    words_data.remove(current_card)
    data = pandas.DataFrame(words_data)
    data.to_csv("./data/words_to_learn.csv",index=False)
    next_card()

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
right_button = Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(column=1,row=1)
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)


# calling the next card function so it does not show us the initial card phase 
# so as soon as we run we will see the french word and not the title and word 
next_card()

# window control
window.mainloop()