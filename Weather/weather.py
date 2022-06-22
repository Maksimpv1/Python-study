from pyowm import OWM
from pyowm.utils import config as cfg
from pyowm.utils import timestamps


config = cfg.get_default_config()
config['language'] = 'ru'

owm = OWM('7e29a3fa39100e53be64a3a2b19bed3d',config)
mgr = owm.weather_manager()

place = input("Какой город вас интересует? ")
observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]
print("В городе " + place + " сейчас примерно " + str(temp))
print("Так же тут " + w.detailed_status)

if temp <= 10:
    print("Холодно одеваться надо теплее")
elif temp <= 20:
    print("Будет тепло, но шорты рано")
elif temp > 20:
    print("Жара одевай что хочешь")