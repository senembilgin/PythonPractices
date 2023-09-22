class Weather:
    def __init__(self, temperature, wind_speed, wind_direction):
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction

    def weather_data(self):
        print(f'The temperature is {self.temperature} C, the wind is coming from {self.wind_direction} and its speed is {self.wind_speed} km/h ')

temp = input('Enter the temperature: ')
w_speed = input('Enter the wind speed: ')
w_direction = input('Enter the direction of the wind: ')

weather = Weather(temp, w_speed, w_direction)
weather.weather_data()

class VerbalWeather(Weather):

    def attribute_wind(self):
        if int(temp) > 20:
            print('It is hot.')
        elif 15 < int(temp) < 20:
            print('It is not hot and not cold.')
        elif int(temp) < 15:
            print('It is cold.')
        if int(w_speed) > 30:
            print('It is windy.')
        elif int(w_speed) < 30:
            print('It is not windy.')

weather_attribute = VerbalWeather(temp,w_speed,w_direction)
weather_attribute.attribute_wind()