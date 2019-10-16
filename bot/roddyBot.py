# coding: utf8
import telebot
import json

bot = telebot.TeleBot("824465608:AAG1U3q3CzxLX0aYHNfX4Eyk4-Eldv-XK9Q")
menu_keyboard = json.dumps({'keyboard': [["/crear_personaje"]], 'one_time_keyboard': True, 'resize_keyboard': True})
option1_keyboard = json.dumps({'keyboard': [["/1"], ["/2"]], 'one_time_keyboard': True, 'resize_keyboard': True})

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    #print(message.chat.id)

    if message.text == "/start":
        	bot.send_message(message.chat.id, """Bienvenido a roddyBot!! \n \n Un bot en el que vivirás miles de aventuras!""", reply_markup = menu_keyboard)
    elif message.text == "/help":
        bot.send_message(message.chat.id, """Lista de comandos!! \n\n /start - Te permite iniciar el bot \n /help muestra los comandos posibles \n /character""")

@bot.message_handler(commands=['crear_personaje'])
def create_character(message):
    """Funció que permet crear un personatge dins de roddyBot"""
    bot.send_message(message.chat.id, "Bienvenido al menú de creación de personaje.")
    bot.send_message(message.chat.id, "¿En que puedo ayudarte? \n \n 1- Ayuda con la creación \n \n 2- crear_personaje", reply_markup = option1_keyboard)

@bot.message_handler(commands=['1','2'])
def menu_info(message):
    if message.text == "/1":
        bot.reply_to(message, """
        Para crear un personaje necesitarás introducir los siguientes parámetros cómo será mostrado en el ejemplo:
        \n \n nombre [nombre personaje]
        \n \n edad [edad personaje]
        \n \n clase [Clase de tu personaje] (es 100% decorativo)
        \n \n apariencia [pequeña descripción]
        \n \n personalidad [describir personalidad]
        \n \n histroria [pequeña historia de tu personaje]""")
        
        create_character(message)



bot.polling(none_stop=True)
