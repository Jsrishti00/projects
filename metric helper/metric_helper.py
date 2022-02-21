# Metric Helper


import tkinter
from tkinter import *
from tkinter import ttk


#Define Window 
root = tkinter.Tk()
root.title('Metric Helper')
root.iconbitmap('ruler.ico')
root.resizable(0,0)

# Define fonts and colours 
field_font = ('Cambria',10)
bg_color = '#c75c5c'
button_color = '#f5cf87'
root.config(bg=bg_color)

# use image colorpicker.com

# Defining functions
def convert():
    """Convert from one metric prefix to another"""
    metric_values = {
        'femto': 10**-15,
        'pico' : 10**-12,
        'nano' : 10**-9,
        'micro': 10**-6,
        'mili' : 10**-3,
        'centi': 10**-2,
        'deci' : 10**-1,
        'base value': 10**0,
        'deca' : 10**1,
        'hecto': 10**2,
        'kilo' : 10**3,
        'mega' : 10**6,
        'giga' : 10**9,
        'tera' : 10**12,
        'peta' : 10**15
    }

    # Clear output field
    output_field.delete(0, END)

    # Get all user info
    start_value = float(input_field.get())
    start_prefix = input_combobox.get()
    end_prefix = output_combobox.get()

    # Convert input to base unit 
    base_value = start_value*metric_values[start_prefix]

    #Convert to new metric value 
    end_value = base_value/metric_values[end_prefix]

    #Update Output field
    output_field.insert(0, str(end_value))

# Define Layout
#  Create the input and output fields
input_field = tkinter.Entry(root, width=20, font=field_font, borderwidth=3 )
output_field = tkinter.Entry(root , width=20 , font=field_font, borderwidth=3 )
equal_label = tkinter.Label(root, text="=" , font=field_font ,bg=bg_color)

# Putting widgets on the screen 
input_field.grid(row=0,column=0,padx=10 , pady=10)
equal_label.grid(row=0,column=1, padx=10 , pady=10)
output_field.grid(row=0,column=2, padx=10 , pady=10)

# Prompt User To enter entry
input_field.insert(0,"Enter You Quantity")

# creating drop down for metric values 
metric_list = ['fento', 'pico', 'nano', 'micro', 'mili', 'centi', 'deci', 'base value', 'deca', 'hecto', 'kilo', 'mega', 'giga','tera', 'peta']

#Create combobox for metric values combobox is just a modern look of drop down
# ttk widgets are more modern widgets

input_combobox = ttk.Combobox(root, value= metric_list , font=field_font , justify='center')
output_combobox = ttk.Combobox(root, value= metric_list , font=field_font , justify='center')
to_label = tkinter.Label(root , text = "to", font=field_font, bg=bg_color)

input_combobox.grid(row =1 , column=0,padx=10, pady=10)
to_label.grid(row=1 , column = 1 ,padx=10, pady=10)
output_combobox.grid(row=1, column=2 ,padx=10, pady=10)

# setting base value to combobox initially
input_combobox.set('base value')
output_combobox.set('base value')

# creating a conversion button indicating we are performing conversion
convert_button = tkinter.Button(root, text='Convert' , font=field_font, bg= button_color, command= convert)
convert_button.grid(row=2 , column=0, columnspan=3 , padx=10 ,pady=10 , ipadx=50)

# Run Windows Main Loop
root.mainloop()



# just like radio variables need a value to track drop down also accquires
#input_choice = StringVar()
#output_choice = StringVar()

#In tkinter drop down is reffered to as OptionMenu
#input_dropdown = tkinter.OptionMenu(root,input_choice , *metric_list)
#output_dropdown = tkinter.OptionMenu(root, output_choice , *metric_list)

#to_label = tkinter.Label(root , text = "to", font=field_font, bg=bg_color)

#placing widgets to screen 
#input_dropdown.grid(row =1 , column=0)
#to_label.grid(row=1 , column = 1)
#output_dropdown.grid(row=1, column=2)

# setting values for input chice and output choice
#input_choice.set('base value')
#output_choice.set('base value')

