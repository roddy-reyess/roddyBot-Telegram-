# coding: utf8
import telebot
from character import character
import json
import os.path

pj = character()
show = ""
definer = ""
new = ""
username = ""
bot = telebot.TeleBot("824465608:AAG1U3q3CzxLX0aYHNfX4Eyk4-Eldv-XK9Q")
menu_keyboard = json.dumps({'keyboard': [["/crear_personaje"]], 'one_time_keyboard': True, 'resize_keyboard': True})
option1_keyboard = json.dumps({'keyboard': [["/ayuda"], ["/crear"]], 'one_time_keyboard': True, 'resize_keyboard': True})
option2_keyboard = json.dumps({'keyboard': [["/guardar"],["/no_guardar"]], 'one_time_keyboard': True, 'resize_keyboard': True})

def checkFile(file_tofill):
    return os.path.isfile(str(file_tofill))

def saveCharVal(user_file):
    charDoc = open(str(user_file)+".txt", 'a')
    charDoc.write(pj.charDict["nombre"]+";"+pj.charDict[])

def fillVariables(new):
    list = ""
    modifier = ""
    for i in new:
        if i != new[0]:
            list = list + i + " "
        else:
            modifier = modifier + i
            modifier = modifier.replace(modifier[0], "")
    return list, modifier

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

@bot.message_handler(commands=['ayuda','crear'])
def menu_info(message):
    if message.text == "/ayuda":

        bot.send_message(message.chat.id, """
        Para crear un personaje necesitarás introducir los siguientes parámetros cómo será mostrado en el ejemplo:
        \n \n nombre [nombre personaje]
        \n \n edad [edad personaje]
        \n \n clase [Clase de tu personaje] (es 100% decorativo)
        \n \n apariencia [pequeña descripción]
        \n \n personalidad [describir personalidad]
        \n \n histroria [pequeña historia de tu personaje]""")
        create_character(message)

    elif message.text =="/crear":
        username = message.chat.first_name

        if checkFile(str(username)+".txt") == True:
            bot.send_message(message.chat.id, "Ya tienes un personaje.")
        else:
            bot.send_message(message.chat.id,"""...\n...\n...\n...\n...\n...\nINICIANDO PROCESO DE CREACIÓN DE PERSONAJE\n...\n...\n...\n...\n...\n...""")
            documentoPj = open (str(username) + ".txt", "w")
            documentoPj.write("nombre ; edad ; clase ; apariencia ; personalidad ; historia" + "\n")
            documentoPj.close()

@bot.message_handler(commands=['nombre'])
def addNameChar(message):
    new = message.text.split()
    show, definer = fillVariables(new)
    pj.addField(definer, show)
    bot.send_message(message.chat.id,"Tu nombre ha sido añadido. Bienvenido " + str(show) + ".")

@bot.message_handler(commands=['edad'])
def addAgeChar(message):
    new = message.text.split()
    show, definer = fillVariables(new)
    pj.addField(definer, show)
    bot.send_message(message.chat.id,"Tienes " + str(show) + "años.")

@bot.message_handler(commands=['clase'])
def addAgeChar(message):
    new = message.text.split()
    show, definer = fillVariables(new)
    #print(show + "//////" + definer)
    pj.addField(definer, show)
    bot.send_message(message.chat.id,"Tu clase es " + str(show) + ". \n Vaya, ¡Eres increible!")

@bot.message_handler(commands=['apariencia'])
def addAgeChar(message):
    new = message.text.split()
    show, definer = fillVariables(new)
    #print(show + "//////" + definer)
    pj.addField(definer, show)
    bot.send_message(message.chat.id,"Eso es bueno, pensaba que eras un hombre sin cara y me asusté.")

@bot.message_handler(commands=['personalidad'])
def addAgeChar(message):
    new = message.text.split()
    show, definer = fillVariables(new)
    #print(show + "//////" + definer)
    pj.addField(definer, show)
    bot.send_message(message.chat.id,"Ahora siento que te conozco mejor.")

@bot.message_handler(commands=['historia'])
def addAgeChar(message):
    new = message.text.split()
    show, definer = fillVariables(new)
    #print(show + "//////" + definer)
    pj.addField(definer, show)
    bot.send_message(message.chat.id,"Veo que tienes una historia... Algún día te contaré la mía, amigo.")

@bot.message_handler(commands=['estatus'])
def creationStatus(message):
    missingElements = pj.charCheck()
    if len(missingElements) >= 1:
        bot.send_message(message.chat.id, "Faltan los siguientes campos por rellenar: " + str(missingElements) + ".")
    else:
        bot.send_message(message.chat.id, "¡Todos los campos creados! ¿Quieres guardar los cambios en tu fichero de personaje?", reply_markup = option2_keyboard)

@bot.message_handler(commands=['guardar','no_guardar'])
def saveCharValues(message):
    if message.text == "/guardar":
        username = message.chat.first_name
        if checkFile(str(username) + ".txt") == True:
            saveCharVal(str(username))
    else:
        pj.removeAllFields()



bot.polling(none_stop=True)
