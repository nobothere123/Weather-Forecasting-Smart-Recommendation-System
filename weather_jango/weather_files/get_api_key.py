###################################################################################################################
#                               get API KEYS                                                                      #
###################################################################################################################

from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

def get_weather_apikey():
    """Retrieve API key from Parameter Store."""
    try:
        api_key = os.getenv('WEATHER_API_KEY')
        return api_key
    except Exception as e:
        print(f"Error: {str(e)}")

weather_api_key = get_weather_apikey()
# print(weather_api_key)

def get_ml_model():
    """Retrieve ml model from Parameter Store."""
    try:
        ml_model = os.getenv('MODEL')
        return ml_model
    except Exception as e:
        print(f"Error: {str(e)}")

ml_model = get_ml_model()
# print(ml_model)

def timezonedb_apikey():
    """Retrieve ml model from Parameter Store."""
    try:
        timezonedb_key = os.getenv('TIMEZONEDB_KEY')
        return timezonedb_key
    except Exception as e:
        print(f"Error: {str(e)}")

timezonedb_key = timezonedb_apikey()
# print(timezonedb_key)

def mongo_client():
    """Retrieve MongoDB client string from environment variable."""
    try:
        mongo_con_string = os.getenv('client_con_string')
        # print(mongo_con_string)
        
        if not mongo_con_string:
            raise ValueError("MongoDB connection string not found in environment variables.")
        return mongo_con_string
    except Exception as e:
        print(f"Failed to extract MongoDB connection string: {e}")
        return mongo_con_string

client_conn_string=mongo_client()
# print(client_conn_string)
client=pymongo.MongoClient(client_conn_string)
db = client.weather_gen