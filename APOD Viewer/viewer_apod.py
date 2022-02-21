import tkinter, requests,webbrowser
from tkcalendar import DateEntry
from tkinter import messagebox, filedialog
from tkinter import *
from PIL import ImageTk , Image
from io import BytesIO

#Define Window
root = tkinter.Tk()
root.title('APOD Photo Viewer')
root.iconbitmap('rocket.ico')

#Define fonts and colors 
text_font =('Times New Roman', 14)
nasa_blue ="#043c93"
nasa_light_blue ="#7aa5d3"
nasa_red ="#ff1923"
nasa_white ="#ffffff"
root.config(bg=nasa_blue)

#Define functions
def quit():
    question = messagebox.askyesno("Close note", "Are you sure you want to close your note and exit the program? ")
    if question == 1:
        root.destroy()

def get_request():
    """ Get request data from NASA and API """
    global response

    #Set the parameters for the request
    url = "https://api.nasa.gov/planetary/apod"
    api_key = "nu7F5oG6rFpYAjw9Gee6TDhq1B3AX1BebuLwrM8L"
    date = calendar.get_date()
    
    querystring = {'api_key' : api_key, 'date':date}
    #call the request and convert it into a python usable format
    response = requests.request("GET", url, params= querystring)
    response = response.json()
    
    #Update output labels
    set_info()

    
def set_info():
    """ Update output labels based on API call """
    #Example response

    #{'copyright': 'Daniel Feller', 'date': '2022-02-11', 
    # 'explanation': "Similar in size to large, bright spiral galaxies in our neighborhood, IC 342 is a mere 10 million light-years distant in the long-necked, northern constellation Camelopardalis. A sprawling island universe, IC 342 would otherwise be a prominent galaxy in our night sky, but it is hidden from clear view and only glimpsed through the veil of stars, gas and dust clouds along the plane of our own Milky Way galaxy. Even though IC 342's light is dimmed and reddened by intervening cosmic clouds, this sharp telescopic image traces the galaxy's own obscuring dust, young star clusters, and glowing pink star forming regions along spiral arms that wind far from the galaxy's core. IC 342 may have undergone a recent burst of star formation activity and is close enough to have gravitationally influenced the evolution of the local group of galaxies and the Milky Way.", 
    # 'hdurl': 'https://apod.nasa.gov/apod/image/2202/IC342Feller.jpg', 'media_type': 'image', 'service_version': 'v1', 
    # 'title': 'IC 342: The Hidden Galaxy in Camelopardalis', 'url': 'https://apod.nasa.gov/apod/image/2202/IC342Feller1024.jpg'}

    #Set info
    #Update the picture date and explanation

    picture_date.config(text = response['date'])
    picture_explanation.config(text = response['explanation'])
    
    #We need to use 3 images in other functions ; an img , a thumb , and a full_img
    global img 
    global thumb 
    global full_img

    url = response['url']

    if response['media_type'] == 'image':
        #Grab the photo that is stored in our response
        img_response = requests.get(url, stream=True ) #Stream = True to automatically download image

        #Get the content of the response and use BytesIo to open it as an image
        #Keep a reference to this img as this is what we can use to save the image(Image not PhotoImage)
        #Create the full screen image for a second window 
        img_data = img_response.content #this is just a string
        img = Image.open(BytesIO(img_data)) #BytesIO to open img data
    
        full_img = ImageTk.PhotoImage(img)

        #Create the thumbnail for the main screen
        thumb_data = img_response.content
        thumb = Image.open(BytesIO(thumb_data))
        thumb.thumbnail((200,200))
    
        thumb = ImageTk.PhotoImage(thumb)

        #Set the thumbnail image 
        picture_label.config(image= thumb)
    
    elif response['media_type'] == 'video':
        #Open video
        picture_label.config(text=url,image='')
        webbrowser.open(url)

def full_photo():
    """ Open the full size photo in new window """
    top = tkinter.Toplevel()
    top.title("Full APOD Photo")
    top.iconbitmap('rocket.ico')

    #Load the full image to the top window
    img_label = tkinter.Label(top, image=full_img)
    img_label.pack()

def save_photo():
    """ Save the desired photo """
    save_name = filedialog.asksaveasfilename(initialdir="./", title="Save Image", filetypes=(("JPEG","*.jpg"),("ALL FILES", "*.*")))
    full_img.save(save_name, + ".jpg")

#Define layout
#Create frames
input_frame = tkinter.Frame(root, bg=nasa_blue)
output_frame = tkinter.Frame(root, bg=nasa_white)
input_frame.pack()
output_frame.pack(padx=50, pady=(0,25))

input_frame.pack()
output_frame.pack(padx=50 , pady=(0,25))

#Layout for input frame 
calendar = DateEntry(input_frame, width=10, font = text_font, background =nasa_blue, foreground = nasa_white )
submit_button = tkinter.Button(input_frame, text= "Submit", font= text_font, bg=nasa_light_blue, command=get_request)
full_button = tkinter.Button(input_frame, text="Full Photo", font=text_font, bg=nasa_light_blue,command=full_photo)
save_button = tkinter.Button(input_frame, text="Save Photo", font= text_font, bg=nasa_light_blue,command=save_photo)
quit_button = tkinter.Button(input_frame, text="Exit",font=text_font ,bg=nasa_red, command=quit )

calendar.grid(row=0 , column = 0, padx= 5 , pady= 10)
submit_button.grid(row=0, column=1, padx= 5 , pady= 10, ipadx=35)
full_button.grid(row=0, column=2, padx= 5 , pady= 10,ipadx=25)
save_button.grid(row=0, column=3, padx= 5 , pady= 10,ipadx=25)
quit_button.grid(row=0, column=4, padx= 5 , pady= 10, ipadx=50)

#Layout for the output frame
picture_date = tkinter.Label(output_frame, text=" ", font= text_font, bg= nasa_white)
picture_explanation = tkinter.Label(output_frame, text=" ", font= text_font, bg= nasa_white, wraplength=600)
picture_label =  tkinter.Label(output_frame, text=" ")

picture_date.grid(row=1,column=1,padx=10)
picture_explanation.grid(row=0,column=0,padx=10,pady=10,rowspan=2)
picture_label.grid(row=0,column=1, padx=10,pady=10)

#Get todays photo
get_request()

#Run windows main loop
root.mainloop()

#https://api.nasa.gov/planetary/apod?api_key=nu7F5oG6rFpYAjw9Gee6TDhq1B3AX1BebuLwrM8L