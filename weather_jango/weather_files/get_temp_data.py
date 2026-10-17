from get_api_key import *
import requests
import json
from datetime import datetime,timedelta
import time
import pandas as pd
from location import get_location

loc_data = [
  {"state": "Andhra Pradesh", "lat": 15.9129, "lon": 79.7400},
  {"state": "Arunachal Pradesh", "lat": 28.2180, "lon": 94.7278},
  {"state": "Assam", "lat": 26.2006, "lon": 92.9376},
  {"state": "Bihar", "lat": 25.0961, "lon": 85.3131},
  {"state": "Chhattisgarh", "lat": 21.2787, "lon": 81.8661},
  {"state": "Goa", "lat": 15.2993, "lon": 74.1240},
  {"state": "Gujarat", "lat": 22.2587, "lon": 71.1924},
  {"state": "Haryana", "lat": 29.0588, "lon": 76.0856},
  {"state": "Himachal Pradesh", "lat": 31.1048, "lon": 77.1734},
  {"state": "Jharkhand", "lat": 23.6102, "lon": 85.2799},
  {"state": "Karnataka", "lat": 15.3173, "lon": 75.7139},
  {"state": "Kerala", "lat": 10.8505, "lon": 76.2711},
  {"state": "Madhya Pradesh", "lat": 22.9734, "lon": 78.6569},
  {"state": "Maharashtra", "lat": 19.7515, "lon": 75.7139},
  {"state": "Manipur", "lat": 24.6637, "lon": 93.9063},
  {"state": "Meghalaya", "lat": 25.4670, "lon": 91.3662},
  {"state": "Mizoram", "lat": 23.1645, "lon": 92.9376},
  {"state": "Nagaland", "lat": 26.1584, "lon": 94.5624},
  {"state": "Odisha", "lat": 20.9517, "lon": 85.0985},
  {"state": "Punjab", "lat": 31.1471, "lon": 75.3412},
  {"state": "Rajasthan", "lat": 27.0238, "lon": 74.2179},
  {"state": "Sikkim", "lat": 27.5330, "lon": 88.5122},
  {"state": "Tamil Nadu", "lat": 11.1271, "lon": 78.6569},
  {"state": "Telangana", "lat": 18.1124, "lon": 79.0193},
  {"state": "Tripura", "lat": 23.9408, "lon": 91.9882},
  {"state": "Uttar Pradesh", "lat": 26.8467, "lon": 80.9462},
  {"state": "Uttarakhand", "lat": 30.0668, "lon": 79.0193},
  {"state": "West Bengal", "lat": 22.9868, "lon": 87.8550},
  {"state": "Delhi", "lat": 28.7041, "lon": 77.1025},
  {"state": "Jammu and Kashmir", "lat": 33.2778, "lon": 75.3412},
  {"state": "Ladakh", "lat": 34.1526, "lon": 77.5770},
  {"state": "Puducherry", "lat": 11.9416, "lon": 79.8083},
  {"state": "Chandigarh", "lat": 30.7333, "lon": 76.7794},
  {"state": "Andaman and Nicobar Islands", "lat": 11.7401, "lon": 92.6586},
  {"state": "Dadra and Nagar Haveli and Daman and Diu", "lat": 20.1809, "lon": 73.0169},
  {"state": "Lakshadweep", "lat": 10.5667, "lon": 72.6417}
]


def get_weather_data(lat, lon,geo_state,temp_date):
    data ={}
    



data ={}
geo_data = get_location()   
geo_loc= geo_data['loc'].split(",")
lat = geo_loc[0]
lon = geo_loc[1] 
geo_ip = geo_data['ip']
geo_city = geo_data['city']
geo_country = geo_data['country']
geo_state = geo_data['region']
geo_postal = geo_data['postal']
geo_timezone = geo_data['timezone']