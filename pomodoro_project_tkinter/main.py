from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Project")
window.config(width=100,height=50,bg=YELLOW)
text = "✔"
# image 
# canvas widget
# same height and width as of the image
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
# half of canvas
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

# label
timer_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW)
timer_label.grid(column=1,row=0)

checkmarks = Label(text=text,fg=GREEN,bg=YELLOW)
checkmarks.grid(column=1,row=3)

# buttons
start_button = Button(text="Start",bg=YELLOW,highlightthickness=0)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",bg=YELLOW,highlightthickness=0)
reset_button.grid(column=2,row=2)





window.mainloop()