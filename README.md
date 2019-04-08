# weather_utils

# Example of how to use weather_utils.py

from weather_utils import Weather

# Set city variable
# Example for a valid city value.
# Valid values can be found in https://openweathermap.org
city = 'Jerusalem'


# Set temperature units variable.
# Example for a valid temperature units value.
# Valid values can be: 'kelvin'\'fahrenheit'\'celcius'
temp_units = 'celcius'

# Create object from Weather class
weather_ob = Weather(city, temp_units)
try:
    # Call get_weather method to fetch waether data
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

