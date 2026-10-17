from get_api_key import *
from ollama import chat
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import sys

def train_model(data):
    weather_col = db["weather_data"]
    weather_old_data= list(weather_col.aggregate(
        [
    {
        "$match": {
            "user_city": data["user_city"]
        }
    },
    {
        "$group": {
            "_id": "$temp",
            "humidity": {"$first": "$humidity"},
            "wind_speed": {"$first": "$wind_speed"}
        }
    },
    {
        "$project": {
            "_id": 0,
            "temp": "$_id",
            "humidity": 1,
            "wind_speed": 1
        }
    },
    {
        "$limit": 50
    }
]
    ))
    
    # print(weather_old_data)
    
    if len(weather_old_data) <= 5 :
        # In a real scenario, X_train/y_train would be loaded from a CSV of Delhi's history
        # X: [[temp, humidity, wind]]
        X_train = np.array([[18, 60, 5], [15, 80, 2], [20, 50, 10], [14, 85, 1]])
        y_train = np.array([17, 14, 19, 13])  # tomorrow data for prediction
    else:
        x_data = [[round(whw['temp']- 273.15, 1), whw['humidity'], round(whw['wind_speed']* 3.6, 1)] for whw in weather_old_data]  # [wdt for wdt in whw.values()]
        # print(x_data)
        y_data = [round(whw['temp']- 273.15, 1) for whw in weather_old_data]
        # print(y_data)
        # sys.exit()
        X_train = np.array(x_data)
        y_train = np.array(y_data)


    c_temp = round(data['temp'] - 273.15, 1)   # F to C
    c_humidity = data['humidity']
    c_wind = round(data['wind_speed'] * 3.6, 1)   # m/s to km/h
    
    model = LinearRegression()
    model.fit(X_train, y_train) 
    
    prediction = round(model.predict([[c_temp, c_humidity, c_wind]])[0],1)
    # print(prediction)
    return prediction
    
    
def genrate_ai_response(data):
    c_temp = round(data['temp'] - 273.15, 1)   # F to C
    c_humidity = data['humidity']
    c_wind = round(data['wind_speed'] * 3.6, 1)   # m/s to km/h
    
    ml_pred_temp = train_model(data)
    
    system_role = f"You are a {data['user_city']},{data['user_country']} Weather Specialist and Health Advisor."
    user_prompt = f"""
    ANALYSIS DATA:
    - City: {data['user_city']}
    - Condition: {data['current_weather']}
    - Current Temp: {c_temp}°C
    - Humidity: {c_humidity}%
    - Wind Speed: {c_wind} km/h (Source: {data['wind_speed']} m/s)
    - Visibility: {data['visibility']/1000} km
    
    ML PREDICTION:
    - Tomorrow's Forecasted Temp: {ml_pred_temp}°C
    
    INSTRUCTIONS:
    1. Explain how the {c_humidity}% humidity and {data['current_weather']} will affect 'Real Feel'.
    2. Mention if the {c_wind} km/h breeze is enough to clear the haze.
    3. Compare today's {c_temp}°C with the ML-predicted {ml_pred_temp}°C.
    4. Provide a health tip for Delhi residents.
    """
    response = chat(model=ml_model, messages=[
        {'role': 'system', 'content': system_role},
        {'role': 'user', 'content': user_prompt}
    ])
    
    return response['message']['content']
    
# weather_data = {'current_weather': 'Haze', 'weather_img': 'D:\\weather_project\\weather_files\\weather_icon.png', 'temp': 289.18, 'feels_like': 288.72, 'temp_min': 289.18, 'temp_max': 289.18, 'pressure': 1018, 'humidity': 72, 'sea_level': 1018, 'grnd_level': 992, 'visibility': 2200, 'wind_speed': 2.57, 'wind_deg': 260, 'clouds_all': 27, '_id': 'weather_data_1', 'user_ip': '183.83.157.198', 'user_city': 'Delhi', 'user_country': 'IN', 'user_state': 'Delhi', 'user_postal': '110001', 'user_timezone': 'Asia/Kolkata', 'user_id': 1273294} 

def get_main_data(weather_data):
    return genrate_ai_response(weather_data)

