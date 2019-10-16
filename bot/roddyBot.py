
import telebot

bot = telebot.TeleBot("824465608:AAG1U3q3CzxLX0aYHNfX4Eyk4-Eldv-XK9Q")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message.chat.id)
    if message.text == "/start":
        	bot.send_message(message.chat.id, """Bienvenido a roddybot!! \n \n Un bot hecho para divertirte y pasar un buen rato.""")
    elif message.text == "/help":
        bot.send_message(message.chat.id, """Lista de comandos!! \n\n /start - Te permite iniciar el bot \n /help muestra los comandos posibles \n /character""")

@bot.message_handler(commands=['character'])
def create_character(message):
    personaje = []
    bot.send_message(message.chat.id, "Quieres crear un personaje?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
