import requests
from Jarvis.config import config



def fetch_weather(city):
    """
    City to weather
    :param city: City
    :return: weather
    """
    api_key = config.weather_api_key
    units_format = "&units=metric"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "lat=30.354235&lon=76.369923" + "&appid=" + api_key + units_format
##    complete_url="https://api.openweathermap.org/data/2.5/weather?lat=30.354235&lon=76.369923&appid=3fb3d28185ab8d88934525890ae450b8&units=metric"

    response = requests.get(complete_url)

    city_weather_data = response.json()

    if city_weather_data["cod"] != "404":
        main_data = city_weather_data["main"]
        weather_description_data = city_weather_data["weather"][0]
        weather_description = weather_description_data["description"]
        current_temperature = main_data["temp"]
        current_pressure = main_data["pressure"]
        current_humidity = main_data["humidity"]
        wind_data = city_weather_data["wind"]
        wind_speed = wind_data["speed"]
        sys_data = city_weather_data["sys"]
        name_data=city_weather_data["name"]

        final_response = f"""
        The weather in {name_data} is currently {weather_description} 
        with a temperature of {current_temperature} degree celcius, 
        atmospheric pressure of {current_pressure} hectoPascals, 
        humidity of {current_humidity} percent 
        and wind speed reaching {wind_speed} kilometers per hour"""

        return final_response

    else:
        return "Sorry Sir, I couldn't find the city in my database. Please try again"