import json
from urllib.request import urlopen
from urllib.error import  URLError

class WeatherException(Exception):
    def __init__(self, value):
        self.value = value

class Weather:
    def __init__(self,city_val, temp_units_val='celcius'):
        self.city = city_val
        self.temp_units = temp_units_val
        self.temp_units_str = '&units=metric'
        self.temp = 0
        self.pressure = 0
        self.humidity = 0
        self.temp_min = 0
        self.temp_max = 0
        self.all_data = {}

    def set_temp_units_str(self):
        if self.temp_units == 'celcius':
            self.temp_units_str = '&units=metric'
        elif self.temp_units == 'fahrenheit':
            self.temp_units_str = '&units=imperial'
        else:
            self.temp_units_str = ''

    def get_weather(self):
        if not isinstance(self.city, str):
            print("Error: get_weather method, "
                  "the city provided: %d "
                  "is not of type string as expected" % self.city)
            return False

        if self.temp_units not in ['celcius', 'fahrenheit', 'kelvin']:
            print(r"Error: get_weather method, "
                  "the temp_units_val provided: %s is not valid. "
                  "Only 'celcius', 'ferenhite', 'kelvin' "
                  "are valid values" % self.temp_units)
            return False

        self.set_temp_units_str()
        print('Retrieving info for city: %s' % self.city)
        req = 'http://api.openweathermap.org/data/2.5/weather?q=' + \
            self.city + \
            '&appid=43b4c78dddeb1efeda3ee09b4a079137' + self.temp_units_str
        print('Request = %s' % req)
        try:
            response = urlopen(req)
            data = json.loads(response.read())
            self.all_data = data['main']
            print("get_weather method, all weather data: %s" % self.all_data)
            self.temp = data['main']['temp']
            self.pressure = data['main']['pressure']
            self.humidity = data['main']['humidity']
            self.temp_min = data['main']['temp_min']
            self.temp_max = data['main']['temp_max']
            return True
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
            if hasattr(e, 'code'):
                print('The server could not fulfill the request.')
                print('Error code: ', e.code)
            raise WeatherException('Got URLError Exception')
        except:
            raise WeatherException('Got an Unknown Exception')











