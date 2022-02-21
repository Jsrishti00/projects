#Morse code converter

import tkinter
from tkinter import IntVar
from tkinter import *
from tkinter import messagebox
from winsound import PlaySound
from playsound import playsound
from PIL import ImageTk, Image
import pygame

#Define window
root = tkinter.Tk()
root.title('Morse Code Translator')
root.iconbitmap('morse.ico')
root.geometry('500x350')
root.resizable(0,0)

pygame.mixer.init()

#Define fonts and colors 
button_font = ('Simsun', 10)
root_color = "#778899"
frame_color ="#dcdcdc"
button_color = "#c0c0c0"
text_color = "#f8f8ff"

#Putting colors on screen
root.config(bg=root_color)

#Define Functions
def quit():
    """Ask the user before exit they are sure they want to quit"""
    question = messagebox.askyesno("Close note", "Are you sure you want to close your note and exit the program? ")
    if question == 1:
        root.destroy()

def convert():
  """Call the appropriate conversion function based on the radio button values"""
  #English to morse code
  if language.get()==1:
    get_morse()
  elif language.get()==2:
    get_english()

def get_morse():
  """Convert english message morse code"""
  #string to hold morse code message
  morse_code = ""

  #Get the input text and standardize it to lower case
  text = input_text.get("1.0", END)
  text= text.lower()

  #Remove any letter of symbols not in our dict keys
  for letter in text:
    if letter not in english_to_morse.keys():
      text = text.replace(letter," ")
  
  #Break up into individual words based on space
  word_list = text.split(" ")

  #Turn individual word in word_list to a list of letters
  for word in word_list:
    letters = list(word)
    #For each letter get morse code representation and append it to the string morse_code
    for letter in letters:
      morse_char = english_to_morse[letter]
      morse_code += morse_char

      #Seperate individual letters with a space
      morse_code += " "
    
    #Seperate individual word with a vertical line (|)
    morse_code += '|'

  output_text.insert("1.0", morse_code)


def get_english():
  """Convert a morse code message to english  """
  #String to hold english message
  english_code = ""

  #Get input text
  text = input_text.get("1.0",END)

  #Remove any letter of symbols not in our dict keys
  for letter in text:
    if letter not in morse_to_english.keys():
      text = text.replace(letter,"")
  
  #Break up into individual words based on |
  word_list = text.split("|")

  #Turn individual word in word_list to a list of letters
  for word in word_list:
    letters = word.split(" ")
    #letters = list(word)
    #For each letter get morse code representation and append it to the string english_code
    for letter in letters:
      english_char = morse_to_english[letter]
      english_code += english_char

      #Seperate individual letters with a space
      #english_code += " "
    
    #Seperate individual word with a space
    english_code += ' '

  output_text.insert("1.0", english_code)

def clear():
  """Clear both text fields"""
  input_text.delete("1.0", END)
  output_text.delete("1.0", END)

def play():
  """Play tones for corresponding dots and dashes """
  #Determine where morse code is
  if language.get()==1:
    text = output_text.get("1.0", END)
  elif language.get()==2:
    text = input_text.get("1.0",END)
  
  #Play the tones(., " ", |)
  for value in text:
    if value ==".":
      playsound('dotplay.mp3')
      #pygame.mixer.music.load('dotplay.mp3')
      #pygame.mixer.music.play(loops=0)
      #root.after(100) #Allows to pause the loop
    elif value =="-":
      #pygame.mixer.music.load('dashplay.mp3')
      #pygame.mixer.music.play(loops=0)
      playsound('dashplay.mp3')
      root.after(200)
    elif value ==" ":
      root.after(300)
    elif value =="|":
      root.after(700)
  
def show_guide():
  """Show a morse code guide in a second window"""
  #Image morse needs to be a global variable to put on the window
  #window guide needs to be global to close in another function
  global morse
  global guide

  #Create second window relative to root window
  guide = tkinter.Toplevel()
  guide.iconbitmap('morse.ico')
  guide.title("Morse Code Guide")
  guide.geometry('350x350+' + str(root.winfo_x()+500) + "+" + str(root.winfo_y()))
  guide.config(bg=root_color)

  #Create the image , label , and pack
  morse = ImageTk.PhotoImage(Image.open('morse_chart.jpg'))
  label = tkinter.Label(guide , image=morse, bg=frame_color)
  label.pack(padx=10,pady=10,ipadx=5,ipady=5)

  #Create Close button
  close_button = tkinter.Button(guide, text="Close", font=button_font, bg=button_color, command=hide_guide)
  close_button.pack(padx=10,ipadx=50)
    
  #Disable guide button
  guide_button.config(state=DISABLED)

def hide_guide():
  """Hide the guide"""
  guide_button.config(state=NORMAL)
  guide.destroy()

#Define dictionaries for morse code 
english_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
  'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
'y': '-.--', 'z': '--..', '1': '.----',
'2': '..---', '3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..', '9': '----.',
'0': '-----', ' ':' ', '|':'|', "":"" }

morse_to_english = dict([(value, key) for key, value in english_to_morse.items()])

#Define Layout
#Create Frames
input_frame = tkinter.LabelFrame(root,bg=frame_color)
output_frame = tkinter.LabelFrame(root,bg=frame_color)
input_frame.pack(padx=16,pady=(16,8))
output_frame.pack(padx=16,pady=(8,16))

#Layout for input frame
input_text = tkinter.Text(input_frame,height=8,width=30,bg=text_color)
input_text.grid(row=0,column=1,rowspan= 3 ,padx=5,pady=5)

#Add Radio buttons
language = IntVar()
language.set(1)

morse_button = tkinter.Radiobutton(input_frame,text="English --> Morse Code", variable = language, value = 1, font = button_font, bg=frame_color )
english_button = tkinter.Radiobutton(input_frame,text="Morse Code --> English", variable = language, value = 2 , font = button_font, bg=frame_color )

guide_button = tkinter.Button(input_frame, text = "Guide", font = button_font, bg=button_color,command=show_guide)

morse_button.grid(row=0,column=0 , pady=(15,0))
english_button.grid(row=1 , column=0)
guide_button.grid(row=2, column=0, sticky="WE",padx=10)

#Layout for the output frame 
output_text = tkinter.Text(output_frame, height=9 , width=30, bg=text_color)
output_text.grid(row=0, column=1, rowspan=4,padx=5, pady=5)

convert_button = tkinter.Button(output_frame, text = "Convert",font = button_font, bg=button_color,command = convert)
play_button = tkinter.Button(output_frame, text="Play Morse", font = button_font, bg=button_color, command=play)
clear_button = tkinter.Button(output_frame, text="Clear", font = button_font, bg = button_color, command=clear)
quit_button = tkinter.Button(output_frame, text = "Quit", font = button_font, bg=button_color, command= quit)

convert_button.grid(row=0, column=0, padx=10, ipadx=50) #Convert ipadx defines column width
play_button.grid(row=1, column=0,padx=10, sticky="WE")
clear_button.grid(row=2, column=0,padx=10, sticky="WE")
quit_button.grid(row=3, column=0, sticky="WE",padx=10)

#Run windows main loop
root.mainloop()