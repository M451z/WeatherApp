import requests
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os
import urllib.request
from io import BytesIO
import time

# Put the key here that you got from weatherapi
key = "KEY"

# url to get request
url = "https://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=no"

# create and design the app
app = Tk()
app.title("Weather App")
app.config(background="white")
app.geometry("540x200")

location_text = StringVar()
location_entry = Entry(app, textvariable=location_text)
location_entry.pack()

# Define a function to get weather info
def wInfo(location):
    req = requests.get(url.format(key, location))

    if req:
        json = req.json()
        city = json["location"]["name"]
        country = json["location"]["country"]
        localTime = json["location"]["localtime"]
        temperature = json["current"]["temp_c"]
        condition = json["current"]["condition"]["text"]
        conditionIcon = json["current"]["condition"]["icon"]
        urlfimg = f"https:{conditionIcon}"
        icn = urllib.request.urlretrieve(f"{urlfimg}", "condIcon.png")
        wind = json["current"]["wind_kph"]
        windDir = json["current"]["wind_dir"]
        humidity = json["current"]["humidity"]

        mainImage = Image.open("Images/wImage.png")
        font= ImageFont.load_default()
        draw = ImageDraw.Draw(mainImage)
        draw.text((35, 15), f"{city}/{country}", (10,0,0), font=font)
        draw.text((160, 135), f"{localTime}", (0,0,0), font=font)
        draw.text((70, 65), f"{temperature} °C", (0,0,0), font=font)
        draw.text((300, 45), f"{condition}", (0,0,0), font=font)
        draw.text((320, 87), f"{wind} km/h", (0,0,0), font=font)
        draw.text((318, 107), f"{windDir}", (0,0,0), font=font)
        draw.text((320, 68), f"{humidity}", (0,0,0), font=font)

        icon = Image.open("condIcon.png")
        ic = icon.resize([100,100])
        mainImage.paste(ic, (150, 40), ic)

        mainImage.save("weather.png")
        photo = ImageTk.PhotoImage(Image.open("weather.png"))
        panel = Label(app, image=photo)
        panel.pack(side="bottom")
        

        rs = [city, country, localTime, temperature, condition, conditionIcon, wind, windDir, humidity]
        return rs
    else:
        print("No Data Found")

def search():
    city = location_text.get()
    weather = wInfo(city)
    if weather:
        messagebox.showinfo("That's it!", "Thanks for using the app!\nGive a star to the repository to support me.")
        app.destroy()
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))

Search_btn = Button(app, text="🔍 Search", 
                    width=12, command=search)
Search_btn.pack()

app.mainloop()
# weatherapi.com