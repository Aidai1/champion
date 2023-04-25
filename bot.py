import telebot
import requests
import os
from config import TOKEN, API


bot = telebot.TeleBot(TOKEN)

def get_weather(lat, lon):
  
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}&units=metric'
    
   
    response = requests.get(url)

    
    if response.status_code == 200:
        data = response.json()
        
        city = data['name']
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']

        
        return f'Weather in {city}: {description}\nTemperature: {temp}°C\nFeels like: {feels_like}°C'
    else:
       
        return 'Could not retrieve weather information at this time.'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Hi, send me your location to get the weather.')

@bot.message_handler(content_types=['location'])
def location_message(message):

    lat = message.location.latitude
    lon = message.location.longitude
    print(lat, lon)

    weather = get_weather(lat, lon)
    bot.reply_to(message, weather)

bot.polling()
