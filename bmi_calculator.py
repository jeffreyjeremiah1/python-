import tkinter

def bmi_calculation():
    height = height_entry.get()
    weight = weight_entry.get()
    BMI = (float(weight) / (float(height) * float(height))) * 10000
    final_bmi = round(BMI, 2)
    bmi_result_label["text"] = f"{final_bmi}"
    # conclusion_print_label["text"] = weight_condition
    weight_condition(final_bmi) # Passed the "BMI value" into the "weight_condition function"


def clear_screen():
    height_entry.delete(0, 'end')
    weight_entry.delete(0, 'end')
    bmi_result_label["text"] = " "


def weight_condition(BMI):
    # how can i access the final_bmi from the bmi_calculation function to use the value and check this condition
    # Corrected the "lablel" test part.
    if BMI < 18.5:
        conclusion_print_label.config(text="You are underweight")
    elif BMI < 24.9:
        conclusion_print_label.config(text="You have a normal weight")
    elif BMI < 35:
        conclusion_print_label.config(text="You are Obese")
    else:
        conclusion_print_label.config(text="You are severely Obese")


window = tkinter.Tk()
window.title("BMI CALCULATOR")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50, bg="#9bdeac")


height_label = tkinter.Label(text="height: ", fg="#A5073E", bg="#9bdeac", font=("Arial", 24))
height_label.grid(column=0, row=0)


height_entry = tkinter.Entry(width=7, highlightthickness=0)
height_entry.grid(column=1, row=0)


cm_label = tkinter.Label(text="cm", fg="#306998", bg="#9bdeac", font=("Arial", 16))
cm_label.grid(column=2, row=0)


weight_label = tkinter.Label(text="weight: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
weight_label.grid(column=0, row=1)


weight_entry = tkinter.Entry(width=7, highlightthickness=0)
weight_entry.grid(column=1, row=1)


kg_label = tkinter.Label(text="kg", fg="#306998", bg="#9bdeac", font=("Arial", 16))
kg_label.grid(column=2, row=1)


bmi_label = tkinter.Label(text="BMI: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
bmi_label.grid(column=0, row=2)

bmi_result_label = tkinter.Label(text="0", fg="#306998", bg="#9bdeac", font=("Arial", 24))
bmi_result_label.grid(column=1, row=2)


clear_button = tkinter.Button(text="Clear", highlightbackground="#FFD43B", fg="#306998", bg="#9bdeac", command=clear_screen)
clear_button.grid(column=0, row=3)


calculate_button = tkinter.Button(text="Calculate", highlightbackground="#FFD43B", fg="#306998", bg="#9bdeac", command=bmi_calculation)
calculate_button.grid(column=1, row=3)


conclusion_label = tkinter.Label(text="Conclusion: ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
conclusion_label.grid(column=0, row=4)

conclusion_print_label = tkinter.Label(text=" ", fg="#306998", bg="#9bdeac", font=("Arial", 24))
conclusion_print_label.grid(column=1, row=4)


window.mainloop()
