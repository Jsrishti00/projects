# NOTEPAD

import tkinter 
from tkinter import StringVar, font, scrolledtext, messagebox, filedialog
from tkinter import *
from PIL import ImageTk , Image


#Define Window
root = tkinter.Tk()
root.title('Notepad')
root.iconbitmap('pad.ico')
root.geometry('600x600')
root.resizable(0,0)


#Define Fonts and colors
text_color = '#fffacd'
menu_color = '#dbd9db'
root_color = '#6c809a'

root.config(bg=root_color)

#Define functions 
def change_font(event):
    """Change the given font based on dropbox options"""
    #if in argument we dont write event it will create a error
    if font_option.get()=='none':
        my_font = (font_family.get(), font_size.get())
    else:
        my_font = (font_family.get(), font_size.get(), font_option.get())

    # Change font style
    input_text.config(font= my_font)

def new_note():
    """Create a new note which clear the screen"""
    #Use a message box for confirmation 
    # mesaagebox.askyesno("title", "Description") stores 1 if yes 0 if no
    question = messagebox.askyesno("New Note", "Are you sure you want to clear and start a new note?")

    if question == 1:
        input_text.delete("1.0",END)
    #1.0 is starting index for scrolled text widgets

def close_note():
    """Closes the note i.e quit the program"""
    question = messagebox.askyesno("Close note", "Are you sure you want to close your note and exit the program? ")
    if question == 1:
        root.destroy()
    
def save_note():
    """Saves note """
    #First three lines are saved as font family , size and option
    #Giving user to save as per wish
    #Use filedialpg to get location and name of where/what to save the file as.
    save_name = filedialog.asksaveasfilename(initialdir="./", title="Save Note", filetypes= (("Text Files", "*.txt"),("All files","*.*")))
    with open (save_name , 'w') as f:
        #Font size must be string not int 
        f.write(font_family.get() + "\n")
        f.write(str(font_size.get()) + "\n")
        f.write(font_option.get() + "\n")
        
        #Write remaining text in field in file
        f.write(input_text.get("1.0",END))

def open_note():
    """Open a previously saved note """
    #First three lines of note are font family , size , and option
    #First set the font then load the text
    #Use filedialog to get location and directory of note file
    open_name = filedialog.askopenfilename(initialdir= "./", title='Open note', filetypes= (("Text Files", "*.txt"),("All files","*.*")) )
    with open(open_name, 'r') as f:
        #Clear the current text 
        input_text.delete("1.0",END)

        #First three lines are font family , font size and font option 
        #You must strip the new line char at the end of each line!
        font_family.set(f.readline().strip())
        font_size.set(int(f.readline().strip()))
        font_option.set(f.readline().strip())

        #Call the change font for these .set() and pass an arbitary value
        change_font(1)

        #Read the rest of the file and insert it into the text field
        text = f.read()
        input_text.insert("1.0", text)


#Define Layout 
#Define frames 
menu_frame = tkinter.Frame(root,bg=menu_color)
text_frame = tkinter.Frame(root, bg=text_color)

menu_frame.pack(padx=5 , pady=5)
text_frame.pack(padx=5 , pady=5)

#Menu frame Layout
#create a menu : new,open , save , close , font family ,font size , font option 
new_image = ImageTk.PhotoImage(Image.open('new.png'))
new_button = tkinter.Button(menu_frame, image=new_image, command= new_note)
new_button.grid(row=0 , column=0 , padx= 5 , pady=5)

open_image = ImageTk.PhotoImage(Image.open('open.png'))
open_button = tkinter.Button(menu_frame, image=open_image,command= open_note)
open_button.grid(row=0 , column=1 , padx= 5 , pady=5)

save_image = ImageTk.PhotoImage(Image.open('save.png'))
save_button = tkinter.Button(menu_frame, image=save_image, command=save_note)
save_button.grid(row=0 , column=2 , padx= 5 , pady=5)

close_image = ImageTk.PhotoImage(Image.open('close.png'))
close_button = tkinter.Button(menu_frame, image=close_image, command= close_note)
close_button.grid(row=0 , column=3 , padx= 5 , pady=5)

#Create a list of fonts
families = font.families()
font_family = StringVar()
font_family_drop = tkinter.OptionMenu(menu_frame, font_family, *families, command= change_font)
font_family.set('Terminal')
#Set width so it fits to times new roman and others
font_family_drop.config(width=16)
font_family_drop.grid(row=0, column=4, padx=5 , pady=5)

#List for sizes
sizes = [1,2,3,4,6,10,11,12,14,16,18,20,22,24,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,64,72,96,98]
font_size = IntVar()
font_size_drop = tkinter.OptionMenu(menu_frame,font_size,*sizes, command= change_font)
font_size.set(12)
#Set width to fit
font_size_drop.config(width=2)
font_size_drop.grid(row=0 , column=5 , padx=5 , pady=5)

#Options list
options = ['none', 'bold', 'italic']
font_option = StringVar()
font_option_drop = tkinter.OptionMenu(menu_frame, font_option, *options, command= change_font)
font_option.set('none')
#Set width
font_option_drop.config(width=5)
font_option_drop.grid(row=0,column=6,padx=5,pady=5)

#Layout for the text frame 
my_font = (font_family.get(), font_size.get())

#Create input_text as a scrolltext widget so you can scroll through the text field 
#Set default width and height to be more than the window size so that on the smallest text size , the text field size is constant.
input_text = tkinter.scrolledtext.ScrolledText(text_frame,width= 1000, height= 100, bg= text_color, font= my_font)
input_text.pack()

#Run main loop 
root.mainloop()