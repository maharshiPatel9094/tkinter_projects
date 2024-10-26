from tkinter import *

# functions
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    label3.config(text=f"{km}")

# window activate
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)
# window.minsize(width=500, height=500)

# entry
miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)

# labels
miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

label1 = Label(text="is equal to")  
label1.grid(column=0, row=0)

label3 = Label(text="0")
label3.grid(column=1,row=1)

label2 = Label(text="Km")  
label2.grid(column=2, row=1)

calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=1,row=2)


# keep the screen open
window.mainloop()
