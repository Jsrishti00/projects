# Hello GUI World 

import tkinter
from tkinter import *

from PIL import ImageTk , Image

#Define Window
root = tkinter.Tk()
root.title("Hello GUI World")
root.iconbitmap("wave.ico")
root.geometry("400x400")
#root.resizable(0,0)

#define fonts and colors 
root_color = "#224870"
input_color = "#2a4494"
output_color = "#4ea5d9"
root.config(bg=root_color)

#Define Functions 
def submit_name():
    # Says Hello to user
    if(len(name.get())!= 0):
        if case_style.get()=='normal':
            name_label = tkinter.Label(output_frame,text = "  " + name.get() , bg= output_color)
        elif case_style.get()=='upper':
            name_label = tkinter.Label(output_frame,text = (" " + name.get()).upper() , bg= output_color)
        elif case_style.get()=='lower':
            name_label = tkinter.Label(output_frame,text = ("  " + name.get()).lower() , bg= output_color)
    
    
    # Pack Labell On Screen
    name_label.pack()

    # Clear the entry field for next entry 
    name.delete(0,END)



#Define Layout

#1) Define Frames
input_frame = tkinter.Frame(root,bg=input_color)
output_frame = tkinter.Frame(root,bg=output_color)
input_frame.pack(pady=10)
output_frame.pack(padx=10, pady=(0,10), fill=BOTH , expand = "True")

# Create Widgets
name = tkinter.Entry(input_frame,text="Enter Your Name",width=20)
submit_button = tkinter.Button(input_frame,text ="Submit", command=submit_name)
name.grid(row = 0 ,column = 0,padx=10,pady = 10)
submit_button.grid(row = 0 , column = 1, padx=10, pady=10, ipadx=20)

# Create Radio Buttons For Text Display
case_style = StringVar()
case_style.set('normal')
normal_button = tkinter.Radiobutton(input_frame, text = "Normal Case" , variable = case_style , value = 'normal',bg= input_color)
upper_button = tkinter.Radiobutton(input_frame, text = "Upper Case" , variable = case_style , value = 'upper', bg= input_color)
lower_button = tkinter.Radiobutton(input_frame, text = "Lower Case" , variable = case_style , value = 'lower', bg= input_color)
normal_button.grid(row  = 1 , column = 0, padx =1,pady = 2)
upper_button.grid(row=1,column = 1, padx = 1 , pady=2)
lower_button.grid(row = 2, column = 0, columnspan=2, padx = 1 , pady = 2)
# Add an Image
smile_image = ImageTk.PhotoImage(Image.open('smile.png'))
smile_label = tkinter.Label(output_frame, image= smile_image , bg = output_color)
smile_label.pack()



# Run Root Window main loop
root.mainloop()