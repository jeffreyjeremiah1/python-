from tkinter import *
from tkinter import Button
from menu import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from datetime import datetime
# matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

now = datetime.now()
currentyear = now.year
currentmonth = now.month
currentday = now.day

total_calorie = []
total_fat = []
total_protein = []


window = Tk()  # It creates the GUI
window.title(string="Calorie Calculator")  # Gives a title to the GUI
window.geometry("500x500+500+250")  # Gives the 500x500 gives the dimensions of the GUI. 500+250 allows it to be centered on my screen
window.config(padx=100, pady=100, bg="#9bdeac")


total = 0


labels = ['calories', 'fats', 'protein']
profit = []
colors = ['red', 'blue', 'green']


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
    total_calorie.append(calories(food_entry.get()))
    total_fat.append(fat(food_entry.get()))
    total_protein.append(protein(food_entry.get()))

    print(f"calories = {total_calorie}")
    print(f"protein = {total_protein}")
    print(f"fat = {total_fat}")

    total = 0
    for i in total_calorie:
        total += i
        calorie_value.config(
            text=str(total))  # "str(total)" converts the integer(total) to a string type used for 'text=' input.

    total = 0  # Clear the value in 'total' before summing protein
    for i in total_protein:
        total += i
        protein_value.config(text=str(total))

    total = 0  # Clear the value in 'total' before summing fat
    for i in total_fat:
        total += i
        fat_value.config(text=str(total))


def clear(event):
    calculate_btn["command"] = " "
    food_entry.delete(0, 'end')
    calorie_value.config(text='')
    fat_value.config(text='')
    protein_value.config(text='')
    conclusion_value.config(text='')


    total_calorie.clear()
    total_protein.clear()
    total_fat.clear()


def calories(choice):
    select = choice.lower()
    food = foods[select]["contents"]["calories"]
    profit.append(food)
    return food


def fat(choice):
    select = choice.lower()
    food = foods[select]["contents"]["fats"]
    profit.append(food)
    return food


def protein(choice):
    select = choice.lower()
    food = foods[select]["contents"]["protein"]
    profit.append(food)
    return food


def chart():
    fig = plt.figure(figsize=(5, 4), dpi=100)
    fig.set_size_inches(5, 4)
    fig.set_facecolor("#9bdeac")
    plt.pie(profit, labels=labels, colors=colors,  autopct='%1.1f%%', shadow=True, startangle=140, explode=(0.2, 0, 0),
            wedgeprops={'linewidth': 3})
    plt.axis('equal')
    canvasbar = FigureCanvasTkAgg(fig, master=window)
    canvasbar.draw()
    canvasbar.get_tk_widget().grid(row=8, column=3)
    plt.show(window)


def save():
    calorie_num = calories(food_entry.get())
    fat_num = fat(food_entry.get())
    protein_num = protein(food_entry.get())
    is_okay = messagebox.askokcancel(title="Calorie calculator", message=f"Save file?")
    if is_okay:
        with open("data.txt", "a") as data_file:
            data_file.write(f"calories:{calorie_num} | fats:{fat_num} | protein:{protein_num}| {now}\n")


time = Label(master=window, text=f"Date: {currentday}/{currentmonth}/{currentyear}", fg="#306998", bg="#9bdeac")
time.grid(row=0, column=3)


food_label = Label(master=window, text="Enter Food: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
# This creates a 'label' and gives it a 'name' with a 'font type' and happens in the main 'window' defined above as
# "window = TK()"
food_label.grid(row=1, column=1)  # This positions where the label will be placed on the GUI
food_entry = Entry(window, highlightthickness=0)  # creates an entry windows to enter information
food_entry.focus()
food_entry.grid(row=1, column=2)  # This positions where the entry will be placed on the GUI


calorie_label = Label(master=window, text="Total Calories: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
calorie_label.grid(row=2, column=1)
calorie_value = Label(master=window, text=' ', fg="#306998", bg="#9bdeac")
calorie_value.grid(row=2, column=2,)


fat_label = Label(master=window, text="Total Fat: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
fat_label.grid(row=3, column=1)
fat_value = Label(master=window, text=' ', fg="#306998", bg="#9bdeac")
fat_value.grid(row=3, column=2)


protein_label = Label(master=window, text="Total Protein: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
protein_label.grid(row=4, column=1)
protein_value = Label(master=window, text=' ', fg="#306998", bg="#9bdeac")
protein_value.grid(row=4, column=2)


conclusion_label = Label(master=window, text="Conclusion: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
conclusion_label.grid(row=5, column=1)
conclusion_value = Label(master=window, text=' ', fg="#306998", bg="#9bdeac")
conclusion_value.grid(row=5, column=2)


calculate_btn = Button(window, text="CALCULATE", fg="#306998", bg="#9bdeac", font=("Arial", 24), highlightthickness=0,
                       command=chart)
calculate_btn.grid(row=6, column=1)
calculate_btn.bind("<Button 1>", func=extract_info)  # left click on button goes to the "" function


btn = Button(window, text="ADD", fg="#306998", bg="#9bdeac", font=("Arial", 24), highlightthickness=0, command=add)
btn.grid(row=7, column=1)
btn.bind("<Button 1>", func=add)  # left click on button goes to the "" function


btn = Button(window, text="CLEAR", fg="#306998", bg="#9bdeac", font=("Arial", 24), highlightthickness=0)
btn.grid(row=8, column=1)
btn.bind("<Button 1>", func=clear)  # left click on button goes to the "" function


btn = Button(window, text="SAVE", fg="#306998", bg="#9bdeac", font=("Arial", 24), highlightthickness=0, command=save)
btn.grid(row=9, column=1)
# btn.bind("<Button 1>", func=save)  # left click on button goes to the "" function


window.mainloop()
