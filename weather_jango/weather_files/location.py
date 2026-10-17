import geocoder
from weather_files.main_weather_info import main_function

def get_location():    
    geo_data =  geocoder.ipinfo("me")
    # print(geo_data)
    # print(geo_data.raw['loc'])
    
    # return geo_data.raw
    
    return main_function(geo_data.raw)
    


# print(get_location())