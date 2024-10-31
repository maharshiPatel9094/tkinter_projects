from tkinter import *

# constants
BACKGROUND_COLOR = "#B1DDC6"

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
canvas.create_text(400,150,text="Title",font=("Arial",60,"bold"))
canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"))
# to remove the background color of canvas
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0,row=0,columnspan=2,sticky="nsew")

# buttons 
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image,highlightthickness=0)
right_button.grid(column=1,row=1)
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0)
wrong_button.grid(column=0,row=1)


# window control
window.mainloop()