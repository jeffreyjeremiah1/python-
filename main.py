import tkinter as tk
from tkinter import ttk


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

        for F in (StartPage, PageOne, PageTwo):
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


class PageOne(tk.Frame):


    def __init__(self, parent, controller):

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
            total_body_water_result["text"] = "0"
            percentage_of_body_weight_result["text"] = "0"

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.grid_rowconfigure(0, weight=2)
        label.grid_columnconfigure(0, weight=2)

        age_label = tk.Label(self,text="Age", font=("Arial", 24), bg="grey", bd=1, relief="sunken", justify="center")
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

        sex_label = tk.Label(self, text="Sex")
        sex_label.grid(column=0, row=3)
        sex_entry = ttk.Entry(self)
        sex_entry.grid(column=1, row=3)

        total_body_water_label = tk.Label(self, text="Total body water (volume): ")
        total_body_water_label.grid(column=0, row=4)
        total_body_water_result = tk.Label(self, text="0")
        total_body_water_result.grid(column=1, row=4)

        percentage_of_body_weight = tk.Label(self, text="Percentage of body weight:")
        percentage_of_body_weight.grid(column=0, row=5)
        percentage_of_body_weight_result = tk.Label(self,text="0")
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



app = SeaofBTCapp()
app.mainloop()


