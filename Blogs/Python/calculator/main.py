import tkinter as tk
import math

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("300x400")

# Create an input field where the user can enter their calculation
input_label = tk.Label(root, text="Enter your calculation:")
input_label.pack()

input_field = tk.Entry(root, width=25, borderwidth=5)
input_field.pack()

# Define functions for each mathematical operation
def add():
    num1 = float(input_field.get())
    input_field.delete(0, tk.END)
    num2 = float(input_field.get())
    result = num1 + num2
    tk.result_field.delete(0, tk.END)
    tk.result_field.insert(0, result)
    
def subtract():
    num1 = float(input_field.get())
    input_field.delete(0, tk.END)
    num2 = float(input_field.get())
    result = num1 - num2
    tk.result_field.delete(0, tk.END)
    tk.result_field.insert(0, result)

def multiply():
    num1 = float(input_field.get())
    input_field.delete(0, tk.END)
    num2 = float(input_field.get())
    result = num1 * num2
    tk.result_field.delete(0, tk.END)
    tk.result_field.insert(0, result)
    
def divide():
    num1 = float(input_field.get())
    input_field.delete(0, tk.END)
    num2 = float(input_field.get())
    result = num1 / num2
    tk.result_field.delete(0, tk.END)
    tk.result_field.insert(0, result)
    
def exponent():
    num1 = float(input_field.get())
    input_field.delete(0, tk.END)
    num2 = float(input_field.get())
    result = num1 ** num2
    tk.result_field.delete(0, tk.END)
    tk.result_field.insert(0, result)
    
def log():
    num1 = float(input_field.get())
    input_field.delete(0, tk.END)
    result = math.log(num1)
    tk.result_field.delete(0, tk.END)
    tk.result_field.insert(0, result)
    
def sin():
    num1 = float(input_field.get())
    input_field.delete(0, tk.END)
    result = math.sin(num1)
    tk.result_field.delete(0, tk.END)
    tk.result_field.insert(0, result)
    
# Creating buttons for those opetaters
add_button = tk.Button(root, text="+", padx=40, pady=20, command=add).pack()
subtract_button = tk.Button(root, text="-", padx=40, pady=20, command=subtract).pack()
multiply_button = tk.Button(root, text="*", padx=40, pady=20, command=multiply).pack()
divide_button = tk.Button(root, text="/", padx=40, pady=20, command=divide).pack()
exp_button = tk.Button(root, text="^", padx=40, pady=20, command=exponent).pack()
log_button = tk.Button(root, text="log", padx=40, pady=20, command=log).pack()
sin_button = tk.Button(root, text="sin", padx=40, pady=20, command=sin).pack()
    
# Add a Calculate button to perform the selected operation
def calculate():
    user_input = input_field.get()
    tk.result_field.delete(0, tk.END)
    try:
        result = eval(user_input)
        tk.result_field.insert(0, result)
    except:
        tk.result_field.insert(0, "Error")

calc_button = tk.Button(root, text="Calculate", padx=40, pady=20, command=calculate).pack()

# Create a result field to display the result of the calculation
result_label = tk.Label(root, text="Result:")
root.mainloop()