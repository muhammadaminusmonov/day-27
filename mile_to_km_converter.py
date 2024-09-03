from tkinter import *


def calculate():
    mile = float(user_input.get())
    km = mile * 1.6
    label_num.config(text=f"{round(km, 2)}")


window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=25, pady=18)

user_input = Entry(width=20)
user_input.insert(END, string="0")
user_input.grid(column=1, row=0)

label_mile = Label(text="Miles")
label_mile.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_num = Label(text="0")
label_num.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

button_calculate = Button(text="Calculate", command=calculate)
button_calculate.grid(column=1, row=2)

window.mainloop()
