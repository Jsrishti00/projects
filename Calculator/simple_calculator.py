# Simple calculator

from multiprocessing import Value
import tkinter
from tkinter import *
from tkinter import END

#Define Window 
root = tkinter.Tk()
root.title('Calculator')
root.iconbitmap('calc.ico')
root.geometry('300x400')
root.resizable(0,0)

#Define fonts and colors 
dark_green = '#93af22'
light_green = '#acc253'
white_green = '#edefe0'
button_font = ('Arial', 18)
display_font = ('Arial',30)

#Define functions
def submit_number(number):
    """Add number or decimal to display"""
    #Insert the number or decimal to end of display
    display.insert(END, number)

    # If decimal used once disable it
    if "." in display.get():
        decimal_button.config(state=DISABLED)

def operate(operator):
    """Store First number of expression and operation to be used"""
    global first_number
    global operation

    #Get operator passsed and the value of display . This is the first calculation
    operation =  operator
    first_number = display.get()

    # Delete the value (first_number) from display
    display.delete(0,END)

    #Disable all operator button until equal or clear is presses
    add_button.config(state=DISABLED)
    subtract_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)
    square_button.config(state=DISABLED)

    # Return decimal button to normal state 
    decimal_button.config(state=NORMAL)

def equal():
    """Run the stored operation for two numbers """
    #Perform the desired mathematics
    if operation == 'add':
        Value = float(first_number) + float(display.get())
    elif operation == 'subtract':
        Value = float(first_number) - float(display.get())
    elif operation == 'multiply':
        Value = float(first_number) * float(display.get())
    elif operation == 'divide':
        if(display.get()== "0"):
            Value = "ERROR"
        else :
            Value = float(first_number) / float(display.get())
    elif operation == 'exponent':
        Value = float(first_number) ** float(display.get())
    
    # Remove the current value of display and update it with the answer
    display.delete(0,END)
    display.insert(0,Value)

    # Return Buttons to normal state
    enable_buttons()

def enable_buttons():
    """Enable all buttons on the calculator"""
    add_button.config(state=NORMAL )
    subtract_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    inverse_button.config(state=NORMAL)
    square_button.config(state= NORMAL)

def clear():
    """Clear the display"""
    display.delete(0,END)

    # Return buttons to normal state
    enable_buttons()

def inverse():
    """Calculate inverse of number """
    if(display.get()==0):
        value = "ERROR"
    else:
        value = 1/float(display.get())
    
    #Delete current display value and update with answer
    display.delete(0,END)
    display.insert(0,value)

def square():
    """Calculate sqaure of number"""
    Value = float(display.get())**2

    #Delete current display value and update with answer
    display.delete(0,END)
    display.insert(0, Value)

def negate():
    """Find negation of number"""
    value = float(display.get())*(-1)

    #Delete current display value and update with answer
    display.delete(0,END)
    display.insert(0,value)

#Define GUI Layout
#Create frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)

display_frame.pack(padx=2,pady=(5,20))
button_frame.pack(padx=2, pady=5)

#Layout for display frame
display = tkinter.Entry(display_frame, width= 50, font= display_font, bg= white_green, borderwidth= 5 , justify=RIGHT)
display.pack(padx=5, pady=5)

#Layout for the button frame 
clear_button = tkinter.Button(button_frame,text= "Clear", font= button_font, bg= dark_green , command= clear)
quit_button = tkinter.Button(button_frame,text= "QUIT", font= button_font, bg= dark_green , command=root.destroy)

inverse_button = tkinter.Button(button_frame, text='1/x' , font= button_font,bg= light_green, command=inverse)
square_button = tkinter.Button(button_frame, text='x^2' , font= button_font,bg= light_green, command=square)
exponent_button = tkinter.Button(button_frame, text='x^n' , font= button_font,bg= light_green,command=lambda:operate('exponent'))
divide_button = tkinter.Button(button_frame, text=' / ' , font= button_font,bg= light_green,command=lambda:operate('divide'))
multiply_button = tkinter.Button(button_frame, text=' * ' , font= button_font,bg= light_green,command=lambda:operate('multiply'))
subtract_button = tkinter.Button(button_frame, text=' - ' , font= button_font,bg= light_green,command=lambda:operate('subtract'))
add_button = tkinter.Button(button_frame, text=' + ' , font= button_font,bg= light_green,command=lambda:operate('add'))
equal_button = tkinter.Button(button_frame, text=' = ' , font= button_font,bg= dark_green, command= equal)
decimal_button = tkinter.Button(button_frame, text=' . ' , font= button_font,bg='black' , fg = 'white',command=lambda:submit_number("."))
negate_button = tkinter.Button(button_frame, text='+/-' , font= button_font,bg= 'black', fg ='white', command=negate) #fg is text color


nine_button = tkinter.Button(button_frame, text =' 9 ' ,font=button_font , bg='black', fg='white',command=lambda:submit_number(9))
eight_button = tkinter.Button(button_frame, text =' 8 ' ,font=button_font , bg='black', fg='white',command=lambda:submit_number(8))
seven_button = tkinter.Button(button_frame, text =' 7 ' ,font=button_font , bg='black', fg='white',command=lambda:submit_number(7))
six_button = tkinter.Button(button_frame, text =' 6 ' ,font=button_font , bg='black', fg='white',command=lambda:submit_number(6))
five_button = tkinter.Button(button_frame, text =' 5 ' ,font=button_font , bg='black', fg='white',command=lambda:submit_number(5))
four_button = tkinter.Button(button_frame, text =' 4 ' ,font=button_font , bg='black', fg='white',command=lambda:submit_number(4))
three_button = tkinter.Button(button_frame, text =' 3 ' ,font=button_font , bg='black', fg='white',command=lambda:submit_number(3))
two_button = tkinter.Button(button_frame, text =' 2 ' ,font=button_font , bg='black', fg='white',command=lambda:submit_number(2))
one_button = tkinter.Button(button_frame, text =' 1 ' ,font=button_font , bg='black', fg='white',command=lambda:submit_number(1))
zere_button = tkinter.Button(button_frame, text =' 0 ' ,font=button_font , bg='black', fg='white',command=lambda:submit_number(0))

#first row
clear_button.grid(row=0 , column=0 , columnspan=2 , pady=1, sticky='WE')
quit_button.grid(row=0, column=2, columnspan=2 , pady=1, sticky='WE')

#Second row 
inverse_button.grid(row=1, column=0,pady=1,sticky='WE')
square_button.grid(row=1,column=1,pady=1,sticky='WE')
exponent_button.grid(row=1,column=2,pady=1,sticky='WE')
divide_button.grid(row=1, column=3,pady=1,sticky='WE')

#Third row(Add padding to create size of columns)
seven_button.grid(row=2, column=0,pady=1,sticky='WE',ipadx=13)
eight_button.grid(row=2, column=1,pady=1,sticky='WE',ipadx=13)
nine_button.grid(row=2 , column=2,pady=1,sticky='WE',ipadx=13)
multiply_button.grid(row=2, column=3,pady=1,sticky='WE',ipadx=13)

#Fourth row
four_button.grid(row=3,column=0,pady=1,sticky='WE')
five_button.grid(row=3,column=1,pady=1,sticky='WE')
six_button.grid(row=3, column=2,pady=1,sticky='WE')
subtract_button.grid(row=3, column=3,pady=1,sticky='WE')

#Fifth row
one_button.grid(row=4,column=0,pady=1,sticky='WE')
two_button.grid(row=4,column=1,pady=1,sticky='WE')
three_button.grid(row=4,column=2,pady=1,sticky='WE')
add_button.grid(row=4,column=3,pady=1,sticky='WE')

#Sixth Row
negate_button.grid(row=5, column=0,pady=1,sticky='WE')
zere_button.grid(row=5, column=1,pady=1,sticky='WE')
decimal_button.grid(row=5, column=2,pady=1,sticky='WE')
equal_button.grid(row=5, column=3,pady=1,sticky='WE')


#Run Window Main loop
root.mainloop()
