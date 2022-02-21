#Weather forecast

import tkinter , requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO #Help us turn string into a form which tkinter can open as a image

#Define window 
root = tkinter.Tk()
root.title('Weather Forecast')
root.iconbitmap('weather.ico')
root.geometry('400x400')
root.resizable(0,0)

#Define fonts and colors
sky_color = "#76c3ef"
grass_color = "#aad207"
output_color = "#dcf0fb"
input_color = "#ecf2ae"
large_font = ('SimSun', 14)
small_font = ('Simsun', 10)

#Define Functions 
def search():
    """Use Open weather api to look up current weather conditions given a city/city,country """
    global response

    #Get API response 
    #URL and my api key
    url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = '69520e71d4382a5461d36e249a218fce'

    #Seach by the appropriate query , either city name or zip
    if search_method.get() == 1:
        querystring = {'q': city_entry.get(), 'appid': api_key, 'units': 'imperial'}
    elif search_method.get() == 2:
        querystring ={'zip' : city_entry.get(), 'appid': api_key, 'units': 'imperial'}
    
    #Calling API
    response = requests.request("GET", url, params=querystring)
    response = response.json()
    print(response)

    get_weather()
    get_icon()

    #Example response
    """ {'coord': {'lon': -71.0598, 'lat': 42.3584}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 
    'base': 'stations', 'main': {'temp': 276.96, 'feels_like': 275.97, 'temp_min': 274.53, 'temp_max': 278.74, 'pressure': 1025, 'humidity': 86}, 'visibility': 10000,
     'wind': {'speed': 1.34, 'deg': 113, 'gust': 2.24}, 'clouds': {'all': 100}, 'dt': 1644259166, 'sys': {'type': 2, 'id': 2013408, 'country': 'US', 'sunrise': 1644234673, 'sunset': 1644271536},
      'timezone': -18000, 'id': 4930956, 'name': 'Boston', 'cod': 200}"""

def get_weather():
    """ Grab information from API response and update our weather labels  """
    #Gather the data to be used from the API response 
    city_name = response['name']
    city_lat = str(response['coord']['lat']) #Latitude
    city_lon = str(response['coord']['lon']) #Longitude

    #Grab main weather 
    main_weather = response['weather'][0]['main']
    description = response['weather'][0]['description']

    temp = str(response['main']['temp'])
    feels_like = str(response['main']['feels_like'])
    temp_min = str(response['main']['temp_min'])
    temp_max = str(response['main']['temp_max'])
    humidity = str(response['main']['humidity'])

    #Update output labels 
    city_info_label.config(text=city_name + "(" + city_lat + ", " + city_lon + ")", font=large_font, bg=output_color)
    weather_label.config(text="Weather : " + main_weather + ", " + description, font=small_font, bg= output_color )
    temp_label.config(text="Temperature : " + temp + " F", font= small_font , bg= output_color)
    feels_label.config(text= "Feels Like : " + feels_like + " F", font=small_font, bg=output_color)
    temp_min_label.config(text= "Min Temperature : " + temp_min + " F" , font= small_font, bg= output_color)
    temp_max_label.config(text= "Max Temperature : " + temp_max + " F" , font= small_font, bg= output_color)
    humidity_label.config(text= "Humidity : " + humidity, font= small_font, bg=output_color)

def get_icon():
    """ Get icon from API response """
    global img

    #Get icon id from api response 
    icon_id = response['weather'][0]['icon']
    #print(icon_id)

    #get the icon from correct website 
    url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)

    #Make  a request at the url to download the icon ; stream = TRUE automatically downloads 
    icon_response = requests.get(url, stream=True)
    #print(icon_response)

    #Turn into a form tkinter / python can use 
    img_data = icon_response.content
    #print(img_data)

    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    #print(img)

    #Update Label
    photo_label.config(image=img)

#Define Layout
#Create Frames 
sky_frame = tkinter.Frame(root, bg=sky_color, height=250)
grass_frame = tkinter.Frame(root, bg= grass_color)

sky_frame.pack(fill= BOTH, expand=TRUE)
grass_frame.pack(fill= BOTH, expand=TRUE)

output_frame = tkinter.LabelFrame(sky_frame, bg=output_color, width=325, height=225)
input_frame = tkinter.LabelFrame(grass_frame, bg= input_color, width=325)

output_frame.pack(pady=30)
output_frame.pack_propagate(0) #So that the frame does not shrinks
input_frame.pack(pady=15)

#Output frame layout
city_info_label = tkinter.Label(output_frame, bg=output_color, text=' ')
weather_label = tkinter.Label(output_frame, bg=output_color, text=' ')
temp_label = tkinter.Label(output_frame, bg=output_color, text=' ')
feels_label = tkinter.Label(output_frame, bg=output_color, text=' ')
temp_min_label = tkinter.Label(output_frame, bg=output_color, text=' ')
temp_max_label = tkinter.Label(output_frame, bg=output_color, text=' ')
humidity_label = tkinter.Label(output_frame, bg=output_color, text=' ')
photo_label = tkinter.Label(output_frame, bg=output_color, text=' ')

city_info_label.pack(pady=8)
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack(pady=8)

#Input frame layout
#Create input frame button and entry
city_entry = tkinter.Entry(input_frame, width=20 , font=large_font)
submit_button = tkinter.Button(input_frame, text='Submit', font=large_font, bg=input_color, command=search)

search_method = IntVar()
search_method.set(1)
search_city = tkinter.Radiobutton(input_frame, text='Seach By City Name', variable=search_method, value=1, font=small_font,bg=input_color)
search_zip = tkinter.Radiobutton(input_frame, text='Seach By Zip Code', variable=search_method, value=2, font=small_font,bg=input_color)

city_entry.grid(row=0, column=0, padx=10, pady=(10,0))
submit_button.grid(row=0,column=1, padx=10,pady=(10,0))
search_city.grid(row=1,column=0, pady=2)
search_zip.grid(row=1, column=1,padx=10, pady=2)

#run windows main loop
root.mainloop()