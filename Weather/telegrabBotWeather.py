from distutils.cmd import Command
import telebot
from pyowm import OWM
from pyowm.utils import config as cfg # <- тут внимательно с написанием
from pyowm.utils import timestamps

config = cfg.get_default_config()
config['language'] = 'ru'

owm = OWM('7e29a3fa39100e53be64a3a2b19bed3d', config)
mgr = owm.weather_manager()
bot = telebot.TeleBot("5340499648:AAEhbvZpCuCU4W1EPW50ECmdGocU5UaiQRg")

@bot.message_handler(commands=['start'])
def welcom(message):
    bot.send_message(message.chat.id, "Доброго времени суток,\n" + "Введите название города погоду которого хотите узнать\n" + "/start - запуск бота \n" + "/help - команды бота \n")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "пока не придумал че писать\n")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    try: # обработчик исключений
        observation = mgr.weather_at_place(message.text)
        w = observation.weather #нету () <- потому что observation это атрибут, а не метод
        #bot.reply_to(message, "Howdy, how are you doing?")
        temp = w.temperature('celsius')["temp"]
        answer = "В городе " + message.text + " сейчас примерно " + str(temp) + "\n\n"
        answer += "Так же тут " + w.detailed_status + "\n\n" #нету () <- потому что detailed_status это атрибут, а не метод

        if temp < 10:
            answer +="Холодно одеваться надо теплее"
        elif temp < 20:
            answer +="Будет тепло, но шорты рано"
        elif temp > 20:
            answer +="Жара одевай что хочешь"

        bot.send_message(message.chat.id, answer)
    except:
        bot.send_message(message.chat.id, "Вы ошиблись с названием города")

#bot.infinity_polling() #хз у меня bot.polling(none_stop=True) не пашет 
                       #так же bot.infinity_polling(), True в этом случае лишнее (оно прилетает в timeout=, если его оставить).
bot.polling(none_stop=True)