
import telebot

bot = telebot.TeleBot("824465608:AAG1U3q3CzxLX0aYHNfX4Eyk4-Eldv-XK9Q")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hola, qué tal estás?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
