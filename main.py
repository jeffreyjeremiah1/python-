import tkinter


def water_level_calculator():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    age = float(age_entry.get())
    sex = sex_entry.get()
    if sex == "male":
        TBW = 2.447 - 0.09156 * age + 0.1074 * height + 0.3362 * weight
        TBW = round(TBW, 2)
        percentage = (TBW / weight) * 100
        percentage = round(percentage)
        total_body_water_result["text"] = f"{TBW} kg"
        percentage_of_body_weight_result["text"] = f"{percentage} %"

    else:
        TBW = -2.097 + 0.1069 * height + 0.2466 * weight
        TBW = round(TBW, 2)
        percentage = (TBW / weight) * 100
        percentage = round(percentage)
        total_body_water_result["text"] = f"{TBW} Kg"
        percentage_of_body_weight_result["text"] = f"{percentage} %"


def clear():
    height_entry.delete(0, 'end')
    weight_entry.delete(0, 'end')
    age_entry.delete(0, 'end')
    sex_entry.delete(0, 'end')
    total_body_water_result["text"] = " "
    percentage_of_body_weight_result["text"] = " "


window = tkinter.Tk()
window.title("Total Body Water Level")
window.minsize(width=500, height=400)
window.config(padx=50, pady=50, bg="grey")


age_label = tkinter.Label(text="Age", font=("Arial", 24), bg="grey", bd=1, relief="sunken", justify="center")
age_label.grid(column=0, row=0)
age_entry = tkinter.Entry()
age_entry.grid(column=1, row=0)


height_label = tkinter.Label(text="Height",  font=("Arial", 24), bg="grey", bd=1, relief="sunken", justify="center")
height_label.grid(column=0, row=1)
height_entry = tkinter.Entry()
height_entry.grid(column=1, row=1)


weight_label = tkinter.Label(text="Weight",  font=("Arial", 24), bg="grey")
weight_label.grid(column=0, row=2)
weight_entry = tkinter.Entry()
weight_entry.grid(column=1, row=2)


sex_label = tkinter.Label(text="Sex",  font=("Arial", 24), bg="grey")
sex_label.grid(column=0, row=3)
sex_entry = tkinter.Entry()
sex_entry.grid(column=1, row=3)


space = tkinter.Label(text="", bg="grey")
space.grid(column=0, row=4)


total_body_water_label = tkinter.Label(text="Total body water (volume): ",  font=("Arial", 24), bg="grey")
total_body_water_label.grid(column=0, row=5)
total_body_water_result = tkinter.Label(text="0",  font=("Arial", 24), bg="grey")
total_body_water_result.grid(column=1, row=5)


percentage_of_body_weight = tkinter.Label(text="Percentage of body weight: ", font=("Arial", 24), bg="grey")
percentage_of_body_weight.grid(column=0, row=6)
percentage_of_body_weight_result = tkinter.Label(text="0", font=("Arial", 24), bg="grey")
percentage_of_body_weight_result.grid(column=1, row=6)


calculator = tkinter.Button(text="calculate", highlightbackground="#FFD43B", bg="grey", command=water_level_calculator)
calculator.grid(column=0, row=7)


clear_screen = tkinter.Button(text="clear", highlightbackground="#FFD43B", bg="grey", command=clear)
clear_screen.grid(column=1, row=7)


window.mainloop()