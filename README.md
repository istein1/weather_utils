# weather_utils

# Example of how to use weather_utils.py

from weather_utils import Weather

# Example of setting city variable. Valid values can be found in https://openweathermap.org 
city = 'Jerusalem'


# Example of setting temperature units variable. Valid values can be:'kelvin', 'fahrenheit', 'celcius'
temp_units = 'celcius'

# Create object from Weather class
weather_ob = Weather(city, temp_units)

try:
    if weather_ob.get_weather():

        print("All weather data: %s" % weather_ob.all_data)

        print("Temperature: %s" % weather_ob.temp)

        print("pressure: %s" % weather_ob.pressure)

        print("humidity: %s" % weather_ob.humidity)

        print("Min temperature: %s" % weather_ob.temp_min)

        print("Max temperature: %s" % weather_ob.temp_max)

except WeatherException as e:

    print("WeatherException was caught")

    print("Error is: %s" % e.value)

