from fastapi import FastAPI
from main_weather_info import main_function

app = FastAPI()


@app.get("/weather-predict")

def weather_starter():
    return main_function()

