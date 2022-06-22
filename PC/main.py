import eel
from pyowm import OWM
from pyowm.utils import config as cfg
from pyowm.utils import timestamps

config = cfg.get_default_config()
config['language'] = 'ru'

owm = OWM('7e29a3fa39100e53be64a3a2b19bed3d',config)

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')["temp"]
    return "В городе " + place + " сейчас примерно " + str(temp)
    

eel.init("web")
eel.start("main.html",size = (700,700))