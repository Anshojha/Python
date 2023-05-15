import tkinter as tk

# Create a tkinter window
window = tk.Tk()
window.geometry('1000x1000')
window.title('Employee Salary Calculator')

# Create labels and entry boxes for input
name_label = tk.Label(window, text='Employee Name:')
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

salary_label = tk.Label(window, text='Basic Salary:')
salary_label.pack()
salary_entry = tk.Entry(window)
salary_entry.pack()

# Define a function to calculate the net salary
def calculate_salary():
    basic_salary = float(salary_entry.get())
    if basic_salary > 50000:
        tax = 0.1
    elif basic_salary > 30000:
        tax = 0.05
    else:
        tax = 0
    
    net_salary = basic_salary - (basic_salary * tax)
    result_label.config(text=f'Net Salary: {net_salary:.2f}')

# Create a button to calculate the net salary
calculate_button = tk.Button(window, text='Calculate', command=calculate_salary)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(window)
result_label.pack()

# Start the tkinter event loop
window.mainloop()
