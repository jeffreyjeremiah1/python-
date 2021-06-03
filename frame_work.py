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

        container = tk.Frame(self, bg="black")
        self.geometry("1080x750")
        # self.resizable(False, False)
        # self.backGroundImage = PhotoImage(file="//Users/jeffreyjeremiah/Downloads/background.png")
        # self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        # self.backGroundImageLabel.place(x=0, y=0)

        container.pack(side="top", fill="both", expand=False)
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
        super(StartPage, self).__init__()
        tk.Frame.__init__(self, parent, width=1080, height=750, bg="black")
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.grid_rowconfigure(0, weight=1)
        label.grid_columnconfigure(0, weight=1)

        self.backGroundImage = PhotoImage(file="//Users/jeffreyjeremiah/Downloads/tone.png",)
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.pack()

        self.canvas = Canvas(self, width=750, height=500, bg="grey")
        self.canvas.place(x=150, y=60)

        title = tk.Label(self, text="Welcome to the Lockdown App", font=("Bold", 30), bg="grey")
        title.place(x=300, y=100)

        note1 = tk.Label(self, text="Find your body water level by clicking the BMI calculator button: ", font=("Arial", 16), bg="grey")
        note1.place(x=170, y=250)
        note2 = tk.Label(self, text="Find your body Mass index by clicking the BMI calculator button: ", font=("Arial", 16), bg="grey")
        note2.place(x=170, y=300)
        note3 = tk.Label(self, text="Find your body Mass index by clicking the BMI calculator button: ", font=("Arial", 16),bg="grey")
        note3.place(x=170, y=350)

        button1 = tk.Button(self, text="Body Water Level Calculator", highlightbackground="grey", fg="#306998", bg="black", font=("Arial", 18),
                             command=lambda: controller.show_frame(PageOne))
        button1.place(x=650, y=250)

        button2 = tk.Button(self, text="BMI Calculator", highlightbackground="grey", fg="#306998", bg="white", font=("Arial", 18),
                             command=lambda: controller.show_frame(PageTwo))
        button2.place(x=650, y=300)

        button3 = tk.Button(self, text="Calorie Calculator", highlightbackground="grey", fg="#306998", bg="white", font=("Arial", 18),
                             command=lambda: controller.show_frame(PageThree))
        button3.place(x=650, y=350)


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

        self.backGroundImage = PhotoImage(file="//Users/jeffreyjeremiah/Downloads/tone.png",)
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.pack()

        self.canvas = Canvas(self, width=750, height=500, bg="grey")
        self.canvas.place(x=150, y=60)

        age_label = tk.Label(self, text="Age", bg="grey", font=("Arial", 20))
        age_label.place(x=200, y=100)
        age_entry = tk.Entry(self, fg="grey")
        age_entry.place(x=300, y=100)

        height_label = tk.Label(self, text="Height", font=("Arial", 20), bg="grey")
        height_label.place(x=200, y=130)
        height_entry = tk.Entry(self, fg="grey")
        height_entry.place(x=300, y=130)

        weight_label = tk.Label(self, text="Weight", font=("Arial", 20), bg="grey")
        weight_label.place(x=200, y=160)
        weight_entry = tk.Entry(self, fg="grey")
        weight_entry.place(x=300, y=160)

        var = tk.StringVar(self)
        var.set(options[0])
        var.trace("w", change)
        sex_option = tk.OptionMenu(self, var, options[0], options[1])
        sex_option.place(x=300, y=190)

        total_body_water_label = tk.Label(self, text="Total body water (volume): ", font=("Arial", 20), bg="grey")
        total_body_water_label.place(x=200, y=230)
        total_body_water_result = tk.Label(self, text="0", font=("Arial", 20), bg="grey",  bd=1, relief="sunken", justify="center",)
        total_body_water_result.place(x=450, y=230)

        percentage_of_body_weight = tk.Label(self, text="Percentage of body weight:", font=("Arial", 20), bg="grey")
        percentage_of_body_weight.place(x=200, y=260)
        percentage_of_body_weight_result = tk.Label(self, text="0", font=("Arial", 20), bg="grey", relief="sunken")
        percentage_of_body_weight_result.place(x=450, y=260)

        calculator = ttk.Button(self, text="calculate", command=water_level_calculator)
        calculator.place(x=200, y=330)

        clear_screen = ttk.Button(self, text="clear", command=clear)
        clear_screen.place(x=350, y=330)

        button1 = tk.Button(self, text="Back to home", highlightbackground="grey",
                             command=lambda: controller.show_frame(StartPage))
        button1.place(x=591, y=530)

        button2 = tk.Button(self, text="Page Two", highlightbackground="grey", justify="center",
                             command=lambda: controller.show_frame(PageTwo))
        button2.place(x=707, y=530)

        button3 = tk.Button(self, text="Page Three", highlightbackground="grey",
                             command=lambda: controller.show_frame(PageThree))
        button3.place(x=800, y=530)


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

        self.backGroundImage = PhotoImage(file="//Users/jeffreyjeremiah/Downloads/tone.png",)
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.pack()

        self.canvas = Canvas(self, width=750, height=500, bg="grey")
        self.canvas.place(x=150, y=60)

        height_label = tk.Label(self, text="height: ", font=("Arial", 20), bg="grey")
        height_label.place(x=200, y=100)

        height_entry = ttk.Entry(self)
        height_entry.place(x=300, y=100)

        cm_label = tk.Label(self, text="cm", font=("Arial", 20), bg="grey")
        cm_label.place(x=500, y=100)

        weight_label = tk.Label(self, text="weight: ", font=("Arial", 20), bg="grey")
        weight_label.place(x=200, y=130)

        weight_entry = ttk.Entry(self)
        weight_entry.place(x=300, y=130)

        kg_label = tk.Label(self, text="kg", font=("Arial", 20), bg="grey")
        kg_label.place(x=500, y=130)

        bmi_label = tk.Label(self, text="BMI: ", font=("Arial", 20), bg="grey")
        bmi_label.place(x=200, y=160)

        bmi_result_label = tk.Label(self, text="0", font=("Arial", 20), bg="grey")
        bmi_result_label.place(x=300, y=160)

        clear_button = ttk.Button(self, text="Clear", command=clear_screen)
        clear_button.place(x=300, y=300)

        calculate_button = ttk.Button(self, text="Calculate", command=bmi_calculation)
        calculate_button.place(x=200, y=300)

        conclusion_label = tk.Label(self, text="Conclusion: ", font=("Arial", 20), bg="grey")
        conclusion_label.place(x=190, y=350)

        conclusion_print_label = tk.Label(self, text=" ", font=("Arial", 18), bg="grey")
        conclusion_print_label.place(x=300, y=350)

        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(StartPage))
        button1.place(x=591, y=530)

        button2 = ttk.Button(self, text="Page one",
                             command=lambda: controller.show_frame(PageOne))
        button2.place(x=707, y=530)

        button2 = ttk.Button(self, text="Page three",
                             command=lambda: controller.show_frame(PageThree))
        button2.place(x=800, y=530)


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
