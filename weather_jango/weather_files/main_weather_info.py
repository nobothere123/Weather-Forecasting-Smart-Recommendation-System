###################################################################################################################
#                               call api here                                                                     #
###################################################################################################################
import requests
from get_api_key import *
import pandas as pd
import os
import json
from weather_files.ollama_promt import get_main_data
from datetime import datetime,timedelta,timezone


local_path = os.path.dirname(os.path.abspath(__file__))
weather_col = db["weather_data"]


def get_weather_img(weather_icon):
    img_path =  os.path.join(local_path,"weather_icon.png")
    url = f"http://openweathermap.org/img/wn/{weather_icon}@2x.png"
    # response = requests.get(url)
    # if response.status_code == 200:
        # img_data = response.content
        # with open(img_path, "wb") as img_file:
        #     img_file.write(img_data)
            
    return url

def get_weather_data(lat, lon,geo_city,geo_country,geo_state,geo_postal,geo_timezone):
    data ={}
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api_key}"
    # print(url)
    url_response = requests.get(url)
    temp_file = json.loads(url_response.content)     # temp_file = {"coord":{"lon":77.2088,"lat":28.6139},"weather":[{"id":701,"main":"Mist","description":"mist","icon":"50d"}],"base":"stations","main":{"temp":287.22,"feels_like":286.82,"temp_min":287.22,"temp_max":287.22,"pressure":1018,"humidity":82,"sea_level":1018,"grnd_level":992},"visibility":1500,"wind":{"speed":3.09,"deg":290},"clouds":{"all":20},"dt":1769673255,"sys":{"type":1,"id":9165,"country":"IN","sunrise":1769650856,"sunset":1769689638},"timezone":19800,"id":1260877,"name":"Parliament House, Delhi","cod":200}
    weather_data = temp_file['weather'][0]
    current_weather = weather_data.get("main","--")
    weather_icon = weather_data.get("icon","--")
    weather_img_icon = get_weather_img(weather_icon)
    wind_data = temp_file['wind']
    clouds_data = temp_file['clouds']
    sunset = datetime.fromtimestamp(temp_file['sys']['sunset']).strftime("%d-%m-%Y %H:%M:%S")
    sunrise = datetime.fromtimestamp(temp_file['sys']['sunrise']).strftime("%d-%m-%Y %H:%M:%S")
    
    
    
    main_data = temp_file['main']
    
    data.update({
        "current_weather":current_weather,
        "weather_img":weather_img_icon,
        "temp":main_data.get("temp","--"),
        "feels_like":main_data.get("feels_like","--"),
        "temp_min":main_data.get("temp_min","--"),
        "temp_max":main_data.get("temp_max","--"),
        "pressure":main_data.get("pressure","--"),
        "humidity":main_data.get("humidity","--"),
        "sea_level":main_data.get("sea_level","--"),
        "grnd_level":main_data.get("grnd_level","--"),
        "visibility":temp_file.get("visibility","--"),
        "wind_speed":wind_data.get("speed","--"),
        "wind_deg":wind_data.get("deg","--"),
        "clouds_all":clouds_data.get("all","--"),
        "_id":f"weather_data_{temp_file.get('id','--')}-{geo_city}-{datetime.now().strftime('%d%m%Y+%H%M%S')}",
        "user_city":geo_city,
        "user_country":geo_country,
        "user_state":geo_state,
        "user_postal":geo_postal,
        "user_id":temp_file.get("id","--"),
        "user_timezone":geo_timezone,
        "sunrise":sunrise,
        "sunset":sunset
        })
    
    return data
    
###################################################################################################################
#                                                 Main Code                                                       #
###################################################################################################################    

def main_function(geo_data):
    
    # print(geo_data)   
    geo_loc= geo_data['loc'].split(",")
    lat = geo_loc[0]
    lon = geo_loc[1] 
    geo_city = geo_data['city']
    geo_country = geo_data['country']
    geo_state = geo_data['region']
    geo_postal = geo_data['postal']
    geo_timezone = geo_data['timezone']
    

    if  lat and lon:
        # counter = weather_col.count_documents({}) # check data count so keep requests track !!
        # if counter <=59:   # Daily request limit is 60 for free trail pack !!
        weather_data = get_weather_data(lat, lon,geo_city,geo_country,geo_state,geo_postal,geo_timezone)  
        # print(weather_data)
        result = get_main_data(weather_data)
        weather_data.update({"result_text":result})
        weather_col.insert_one(weather_data)
        # print(result)
        return weather_data
        # else:
        #     print("Daily request limit reached !!")
        #     return "Daily request limit reached !!"

    else:
        print(" Location not found !!")
        return " Location not found !!"
    
