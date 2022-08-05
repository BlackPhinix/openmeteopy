print(__name__)
import pandas as pd
import time

from openmeteo_py import Hourly,Daily,OWmanager,Options
from tkinter import *
from geopy.geocoders import Nominatim

# Create an instance of tkinter frame
win = Tk()

# Define geometry of the window
win.geometry("700x350")

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

# Latitude & Longitude input
coordinates = "17.3850 , 78.4867"

location = geolocator.reverse(coordinates)

address = location.raw['address']

# Traverse the data
city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')

# Create a Label widget
label1=Label(text="Given Latitude and Longitude: " + coordinates, font=("Calibri", 24, "bold"))
label1.pack(pady=20)

label2=Label(text="The city is: " + city, font=("Calibri", 24, "bold"))
label2.pack(pady=20)

label3=Label(text="The state is: " + state, font=("Calibri", 24, "bold"))
label3.pack(pady=20)

label4=Label(text="The country is: " + country, font=("Calibri", 24, "bold"))
label4.pack(pady=20)

win.mainloop()
# Latitude, Longitude for Rabat,Morocco
latitude = 33.9842
longitude = -6.8675

hourly = Hourly()
daily = Daily()
options = Options(latitude,longitude)

mgr = OWmanager(options,
    hourly.cloudcover_mid(),
    daily.temperature_2m_max())


# Download data
meteo = mgr.get_data(1,1,"/home/morpheus/openmeteopy/output")



'''
options :
1 - response JSON
2 - JSON with keys for each variable as the date/time,value is the value at that precise time/date
3 - response as a dataframe
4 - Dataframe as date/value for each variable (each variable has its own dataframe)
/file = true :
save the outpute as a file,depending on the output could be a dataframe or a json file,could also be an xls file or netcdf ...
'''
print(str(meteo['hourly']['cloudcover_mid'])+'\n')
print(str(meteo['daily']['temperature_2m_max'])+'\n')
