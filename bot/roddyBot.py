#-*- coding: utf8 -*-
import telebot
import json
import os.path
import sys
from multiprocessing import Value
from character import character
from inventory import inventory

reload(sys)
sys.setdefaultencoding('utf8')
pj = character()
inv = inventory()
show = ""
definer = ""
new = ""
username = ""
bot = telebot.TeleBot("824465608:AAG1U3q3CzxLX0aYHNfX4Eyk4-Eldv-XK9Q")
menu_keyboard = json.dumps({'keyboard': [["/crear_personaje"]], 'one_time_keyboard': True, 'resize_keyboard': True})
option1_keyboard = json.dumps({'keyboard': [["/ayuda"], ["/crear"]], 'one_time_keyboard': True, 'resize_keyboard': True})
option2_keyboard = json.dumps({'keyboard': [["/guardar"],["/no_guardar"]], 'one_time_keyboard': True, 'resize_keyboard': True})
#a = Value('i', 4)

def checkFile(file_tofill):
    return os.path.isfile(str(file_tofill))

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
        \n\n/nombre [nombre personaje]
        \n\n/edad [edad personaje]
        \n\n/clase [Clase de tu personaje] (es 100% decorativo)
        \n\n/apariencia [pequeña descripción]
        \n\n/personalidad [describir personalidad]
        \n\n/histroria [pequeña historia de tu personaje]
        \n\n/estatus para comprovar que campos faltan o para guardar el personaje""")
        create_character(message)

    elif message.text =="/crear":
        username = "characters/" + message.chat.first_name

        if checkFile(str(username)+".txt") == True:
            bot.send_message(message.chat.id, "Ya tienes un personaje.")
        else:
            bot.send_message(message.chat.id,"""Iniciando proceso de creación de personaje. \nPor favor usa /estatus para revisar que campos faltan por crear.""")
            documentoPj = open (str(username) + "_pj.txt", "w+")
            documentoPj.write("nombre ; edad ; clase ; apariencia ; personalidad ; historia" + "\n")
            documentoPj.close()
            documentoPj = open (str(username) + "_inv.txt", "w+")
            documentoPj.write("objeto ; descripción ; tipo" + "\n")
            documentoPj.close()

@bot.message_handler(commands=['nombre','edad', 'clase', 'apariencia','personalidad','historia'])
def addNameChar(message):
    new = message.text.split()
    show, definer = fillVariables(new)
    pj.addField(definer, show)
    if "/nombre" in message.text:
        bot.send_message(message.chat.id,"Tu nombre ha sido añadido. Bienvenido " + str(show) + ".")
    elif "/edad" in message.text:
        bot.send_message(message.chat.id,"Tienes " + str(show) + "años.")
    elif "/clase" in message.text:
        bot.send_message(message.chat.id,"Tu clase es " + str(show) + ". \n Vaya, ¡Eres increible!")
    elif "/apariencia" in message.text:
        bot.send_message(message.chat.id,"Eso es bueno, pensaba que eras un hombre sin cara y me asusté.")
    elif "/personalidad" in message.text:
        bot.send_message(message.chat.id,"Ahora siento que te conozco mejor.")
    elif "/historia" in message.text:
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
        charFile = "characters/" + str(message.chat.first_name) + "_pj"
        invFile = "characters/" + str(message.chat.first_name) + "_inv"
        if pj.checkFile(str(charFile) + ".txt") == True:
            pj.saveCharVal(str(charFile))
        else:
            documentoPj = open (str(charFile) + ".txt", "w+")
            documentoPj.write("nombre ; edad ; clase ; apariencia ; personalidad ; historia" + "\n")
            documentoPj.close()
            pj.saveCharVal(str(charFile))
        bot.send_message(message.chat.id, "Personaje creado, ahora será añadido tu inventario.")
    else:
        pj.removeAllFields()
@bot.message_handler(commands=['yo'])
def mostraPersonatge(message):
    charFile = "characters/" + str(message.chat.first_name) + "_pj"
    content = checkFileContent(str(charFile)+".txt")
    bot.send_message(message.chat.id, "Mostrando tu personaje:\n\n -------------------------------------- \nnombre: " + str(content[0]) + "\nedad: " + str(content[1]) + "\nclase: " + str(content[2]) + "\napariencia: " + str(content[3]) + "\npersonalidad: " + str(content[4]) + "\nhistoria: " + str(content[5]))

bot.polling(none_stop=True)
