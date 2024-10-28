from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer")
    checkmarks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break",fg=RED)        
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break",fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work",fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# after is method which will run after some milli seconds and take function as second parameter.
def countdown(count):
    
    # "00:00 -> format"
    # 245 sec
    # 245 / 60 = 4 minutes 
    # 245 % 60 =  give us seconds 
    
    count_min = math.floor( count / 60 )
    count_sec = count % 60
    # dynamic typing 
    # changing the data type of variable is called as dynamic typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        # after reaching 0 it will catch again
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += text
        checkmarks.config(text=mark)
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
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

# label
timer_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW)
timer_label.grid(column=1,row=0)

checkmarks = Label(fg=GREEN,bg=YELLOW)
checkmarks.grid(column=1,row=3)

# buttons
start_button = Button(text="Start",bg=YELLOW,highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",bg=YELLOW,highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)





window.mainloop()