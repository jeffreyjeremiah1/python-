import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Button
from tkinter import messagebox
from menu import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime

now = datetime.now()
currentyear = now.year
currentmonth = now.month
currentday = now.day

total_calorie = []
total_fat = []
total_protein = []

labels = ['calories', 'fats', 'protein']
values = []
colors = ['red', 'blue', 'green']

LARGE_FONT = ("verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Lockdown App")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def qf():
    print("you dit it")


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=500, height=400)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.grid_rowconfigure(0, weight=1)
        label.grid_columnconfigure(0, weight=1)

        button1 = ttk.Button(self, text="visit page 1",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="Visit page 2",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Visit page 3",
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):

        def water_level_calculator():
            height = float(height_entry.get())
            weight = float(weight_entry.get())
            age = float(age_entry.get())
            sex = var.get()
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
            total_body_water_result["text"] = "0"
            percentage_of_body_weight_result["text"] = "0"

        options = ["male", "female"]

        def change():
            if var.get() == options[0]:
                return "male"
            else:
                return "female"

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.grid_rowconfigure(0, weight=2)
        label.grid_columnconfigure(0, weight=2)

        age_label = tk.Label(self, text="Age", font=("Arial", 24), bg="grey", bd=1, relief="sunken", justify="center")
        age_label.grid(column=0, row=0)
        age_entry = ttk.Entry(self)
        age_entry.grid(column=1, row=0)

        height_label = tk.Label(self, text="Height")
        height_label.grid(column=0, row=1)
        height_entry = ttk.Entry(self)
        height_entry.grid(column=1, row=1)

        weight_label = ttk.Label(self, text="Weight")
        weight_label.grid(column=0, row=2)
        weight_entry = ttk.Entry(self)
        weight_entry.grid(column=1, row=2)

        var = tk.StringVar(self)
        var.set(options[0])
        var.trace("w", change)
        sex_option = tk.OptionMenu(self, var, options[0], options[1])
        sex_option.grid(column=1, row=3)

        total_body_water_label = tk.Label(self, text="Total body water (volume): ")
        total_body_water_label.grid(column=0, row=4)
        total_body_water_result = tk.Label(self, text="0")
        total_body_water_result.grid(column=1, row=4)

        percentage_of_body_weight = tk.Label(self, text="Percentage of body weight:")
        percentage_of_body_weight.grid(column=0, row=5)
        percentage_of_body_weight_result = tk.Label(self, text="0")
        percentage_of_body_weight_result.grid(column=1, row=5)

        calculator = ttk.Button(self, text="calculate", command=water_level_calculator)
        calculator.grid(column=0, row=6)

        clear_screen = ttk.Button(self, text="clear", command=clear)
        clear_screen.grid(column=1, row=6)

        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(StartPage))
        button1.grid(column=3, row=0)

        button2 = ttk.Button(self, text="Page Two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.grid(column=4, row=0)

        button3 = ttk.Button(self, text="Page Three",
                             command=lambda: controller.show_frame(PageThree))
        button3.grid(column=5, row=0)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):

        def bmi_calculation():
            height = height_entry.get()
            weight = weight_entry.get()
            BMI = (float(weight) / (float(height) * float(height))) * 10000
            final_bmi = round(BMI, 2)
            bmi_result_label["text"] = f"{final_bmi}"
            # conclusion_print_label["text"] = weight_condition
            # return final_bmi
            weight_condition(final_bmi)

        def clear_screen():
            height_entry.delete(0, 'end')
            weight_entry.delete(0, 'end')
            bmi_result_label["text"] = " "

        def weight_condition(BMI):
            # how can i access the final_bmi from the bmi_calculation function to use the value and check this condition
            if BMI < 18.5:
                difference = 18.5 - BMI
                difference = round(difference, 2)
                conclusion_print_label[
                    "text"] = f"You are underweight, you need to gain at least {difference} kg to reach a " \
                              f"healthy BMI"
            elif BMI < 24.9:
                conclusion_print_label["text"] = "You have a healthy weight"
            elif BMI < 35:
                difference = BMI - 18.5
                difference = round(difference, 2)
                conclusion_print_label[
                    "text"] = f"You are obese, you need to loose at least {difference} kg to reach a " \
                              f"healthy BMI"
            else:
                difference = BMI - 18.5
                difference = round(difference, 2)
                conclusion_print_label[
                    "text"] = f"You are severely obese, you need to loose at least {difference} kg to reach" \
                              f"a healthy BMI "

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.grid_rowconfigure(0, weight=2)
        label.grid_columnconfigure(0, weight=2)

        height_label = tk.Label(self, text="height: ")
        height_label.grid(column=0, row=0)

        height_entry = ttk.Entry(self)
        height_entry.grid(column=1, row=0)

        cm_label = tk.Label(self, text="cm")
        cm_label.grid(column=2, row=0)

        weight_label = tk.Label(self, text="weight: ")
        weight_label.grid(column=0, row=1)

        weight_entry = ttk.Entry(self)
        weight_entry.grid(column=1, row=1)

        kg_label = tk.Label(self, text="kg")
        kg_label.grid(column=2, row=1)

        bmi_label = tk.Label(self, text="BMI: ")
        bmi_label.grid(column=0, row=2)

        bmi_result_label = tk.Label(self, text="0")
        bmi_result_label.grid(column=1, row=2)

        clear_button = ttk.Button(self, text="Clear", command=clear_screen)
        clear_button.grid(column=0, row=3)

        calculate_button = ttk.Button(self, text="Calculate", command=bmi_calculation)
        calculate_button.grid(column=1, row=3)

        conclusion_label = tk.Label(self, text="Conclusion: ")
        conclusion_label.grid(column=0, row=4)

        conclusion_print_label = tk.Label(self, text=" ")
        conclusion_print_label.grid(column=1, row=4)

        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(StartPage))
        button1.grid(column=3, row=0)

        button2 = ttk.Button(self, text="Page one",
                             command=lambda: controller.show_frame(PageOne))
        button2.grid(column=4, row=0)

        button2 = ttk.Button(self, text="Page three",
                             command=lambda: controller.show_frame(PageThree))
        button2.grid(column=5, row=0)


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        super(PageThree, self).__init__()

        def extract_info(event):
            error = Label(self, text='')
            error.grid(row=9, column=1)
            if food_entry.get() == '':
                pass  # Add Error code below
                #  Error.config(text="Enter a valid food...")
            else:
                calorie_value.config(text=calories(food_entry.get()))
                fat_value.config(text=fat(food_entry.get()))
                protein_value.config(text=protein(food_entry.get()))
                conclusion_value.config(text="You consumed more than the daily recommended calorie intake")

        def add(event):
            values.clear()
            total_calorie.append(calories(food_entry.get()))
            total_fat.append(fat(food_entry.get()))
            total_protein.append(protein(food_entry.get()))

            print(f"calories = {total_calorie}")
            print(f"protein = {total_protein}")
            print(f"fat = {total_fat}")

            sum_calorie = 0
            for i in total_calorie:
                sum_calorie += i
                values.append(float(sum_calorie))
                calorie_value.config(
                    text=str(
                        sum_calorie))  # "str(total)" converts the integer(total) to a string type used for 'text='
                # input.

            sum_protein = 0  # Clear the value in 'total' before summing protein
            for i in total_protein:
                sum_protein += i
                values.append(float(sum_protein))
                protein_value.config(text=str(sum_protein))

            sum_fat = 0  # Clear the value in 'total' before summing fat
            for i in total_fat:
                sum_fat += i
                values.append(float(sum_fat))
                fat_value.config(text=str(sum_fat))

        def calories(choice):
            select = choice.lower()
            food = foods[select]["contents"]["calories"]
            values.append(food)
            return food

        def fat(choice):
            select = choice.lower()
            food = foods[select]["contents"]["fats"]
            values.append(food)
            return food

        def protein(choice):
            select = choice.lower()
            food = foods[select]["contents"]["protein"]
            values.append(food)
            return food

        def chart():
            fig = plt.figure(figsize=(5, 4), dpi=100)
            fig.set_size_inches(5, 4)
            fig.set_facecolor("#9bdeac")
            plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140,
                    explode=(0.2, 0, 0),
                    wedgeprops={'linewidth': 3})
            plt.axis('equal')
            canvasbar = FigureCanvasTkAgg(fig, self)
            canvasbar.draw()
            canvasbar.get_tk_widget().grid(row=8, column=3)
            plt.show(self)

        def clear(event):
            food_entry.delete(0, 'end')
            calorie_value.config(text='')
            fat_value.config(text='')
            protein_value.config(text='')
            conclusion_value.config(text='')
            total_calorie.clear()
            total_protein.clear()
            total_fat.clear()
            values.clear()
            plt.clf()

        def save():
            calorie_num = calories(food_entry.get())
            fat_num = fat(food_entry.get())
            protein_num = protein(food_entry.get())
            is_okay = messagebox.askokcancel(title="Calorie calculator", message=f"Save file?")
            if is_okay:
                with open("data.txt", "a") as data_file:
                    data_file.write(f"calories:{calorie_num} | fats:{fat_num} | protein:{protein_num}| {now}\n")

        time = Label(self, text=f"Date: {currentday}/{currentmonth}/{currentyear}", fg="#306998", bg="#9bdeac")
        time.grid(row=0, column=3)

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Three!!!", font=LARGE_FONT)
        label.grid_rowconfigure(0, weight=2)
        label.grid_columnconfigure(0, weight=2)

        food_label = Label(self, text="Enter Food: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
        # This creates a 'label' and gives it a 'name' with a 'font type' and happens in the main 'window' defined
        # above as "window = TK()"
        food_label.grid(row=1, column=1)  # This positions where the label will be placed on the GUI
        food_entry = Entry(self, highlightthickness=0)  # creates an entry windows to enter information
        food_entry.focus()
        food_entry.grid(row=1, column=2)  # This positions where the entry will be placed on the GUI

        calorie_label = Label(self, text="Total Calories: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
        calorie_label.grid(row=2, column=1)
        calorie_value = Label(self, text=' ', fg="#306998", bg="#9bdeac")
        calorie_value.grid(row=2, column=2, )

        fat_label = Label(self, text="Total Fat: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
        fat_label.grid(row=3, column=1)
        fat_value = Label(self, text=' ', fg="#306998", bg="#9bdeac")
        fat_value.grid(row=3, column=2)

        protein_label = Label(self, text="Total Protein: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
        protein_label.grid(row=4, column=1)
        protein_value = Label(self, text=' ', fg="#306998", bg="#9bdeac")
        protein_value.grid(row=4, column=2)

        conclusion_label = Label(self, text="Conclusion: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
        conclusion_label.grid(row=5, column=1)
        conclusion_value = Label(self, text=' ', fg="#306998", bg="#9bdeac")
        conclusion_value.grid(row=5, column=2)

        calculate_btn = Button(self, text="CALCULATE", fg="#306998", bg="#9bdeac", font=("Arial", 24),
                               highlightthickness=0,
                               command=chart)
        calculate_btn.grid(row=6, column=1)
        calculate_btn.bind("<Button 1>", func=extract_info)  # left click on button goes to the "" function

        add_btn = Button(self, text="ADD", fg="#306998", bg="#9bdeac", font=("Arial", 24), highlightthickness=0,
                         command=chart)
        add_btn.grid(row=7, column=1)
        add_btn.bind("<Button 1>", func=add)  # left click on button goes to the "" function

        btn = Button(self, text="CLEAR", fg="#306998", bg="#9bdeac", font=("Arial", 24), highlightthickness=0)
        btn.grid(row=8, column=1)
        btn.bind("<Button 1>", func=clear)  # left click on button goes to the "" function

        btn = Button(self, text="SAVE", fg="#306998", bg="#9bdeac", font=("Arial", 24), highlightthickness=0,
                     command=save)
        btn.grid(row=9, column=1)
        # btn.bind("<Button 1>", func=save)  # left click on button goes to the "" function

        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(StartPage))
        button1.grid(column=0, row=0)

        button2 = ttk.Button(self, text="Page one",
                             command=lambda: controller.show_frame(PageOne))
        button2.grid(column=0, row=1)

        button3 = ttk.Button(self, text="Page two",
                             command=lambda: controller.show_frame(PageTwo))
        button3.grid(column=0, row=2)


app = SeaofBTCapp()
app.mainloop()
