from tkinter import *
from tkinter import Button
from menu import *


def extract_info(event):
    Error = Label(master=window, text='')
    Error.grid(row=9, column=1)
    if food_entry.get() == '':
        pass  # Add Error code below
        #  Error.config(text="Enter a valid food...")

    else:
        calorie_value.config(text=calories(food_entry.get()))
        fat_value.config(text=fat(food_entry.get()))
        protein_value.config(text=protein(food_entry.get()))
        conclusion_value.config(text="You consumed more than the daily recommended calorie intake")


def add(event):
    print("add")


def clear(event):
    calorie_value.config(text='')
    fat_value.config(text='')
    protein_value.config(text='')
    conclusion_value.config(text='')


def calories(choice):
    select = choice.lower()
    food = foods[select]["contents"]["calories"]
    return food


def fat(choice):
    select = choice.lower()
    food = foods[select]["contents"]["fats"]
    return food


def protein(choice):
    select = choice.lower()
    food = foods[select]["contents"]["protein"]
    return food


window = Tk()  # It creates the GUI
window.title(string="Calorie Calculator")  # Gives a title to the GUI
window.geometry("500x500+500+250")  # Gives the 500x500 gives the dimensions of the GUI. 500+250 allows it to be centered on my screen
window.config(padx=50, pady=50, bg="#9bdeac")

food_label = Label(master=window, text="Enter Food: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))  # This creates a 'label' and gives it a 'name' with a 'font type' and happens in the main 'window' defined above as "window = TK()"
food_label.grid(row=0, column=1)  # This positions where the label will be placed on the GUI
food_entry = Entry(window, highlightthickness=0)  # creates an entry windows to enter information
food_entry.grid(row=0, column=2)  # This positions where the entry will be placed on the GUI

calorie_label = Label(master=window, text="Total Calories: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
calorie_label.grid(row=1, column=1)
calorie_value = Label(master=window, text='')
calorie_value.grid(row=1, column=2)

fat_label = Label(master=window, text="Total Fat: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
fat_label.grid(row=2, column=1)
fat_value = Label(master=window, text='')
fat_value.grid(row=2, column=2)

protein_label = Label(master=window, text="Total Protein: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
protein_label.grid(row=3, column=1)
protein_value = Label(master=window, text='')
protein_value.grid(row=3, column=2)

conclusion_label = Label(master=window, text="Conclusion: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
conclusion_label.grid(row=4, column=1)
conclusion_value = Label(master=window, text='')
conclusion_value.grid(row=4, column=2)

btn = Button(window, text="CALCULATE", fg="#306998", bg="#9bdeac", font=("Arial", 24), highlightthickness=0)
btn.grid(row=5, column=1)
btn.bind("<Button 1>", func=extract_info)  # left click on button goes to the "" function

btn = Button(window, text="ADD", fg="#306998", bg="#9bdeac", font=("Arial", 24), highlightthickness=0)
btn.grid(row=6, column=1)
btn.bind("<Button 1>", func=add)  # left click on button goes to the "" function

btn = Button(window, text="CLEAR", fg="#306998", bg="#9bdeac", font=("Arial", 24), highlightthickness=0)
btn.grid(row=7, column=1)
btn.bind("<Button 1>", func=clear)  # left click on button goes to the "" function

window.mainloop()
