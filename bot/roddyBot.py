#-*- coding: utf8 -*-
import telebot
import json
import os
import sys
import time
from multiprocessing import Value
from character import character
from inventory import inventory
from object import object
from equip import equip
from readBooks import readBooks

reload(sys)
sys.setdefaultencoding('utf8')
pj = character()
inv = inventory()
allobjects = object()
book = readBooks()
equip = equip()
show = ""
definer = ""
new = ""
username = ""
bot = telebot.TeleBot("824465608:AAG1U3q3CzxLX0aYHNfX4Eyk4-Eldv-XK9Q")
menu_keyboard = json.dumps({'keyboard': [["/crear_personaje"]], 'one_time_keyboard': True, 'resize_keyboard': True})
option1_keyboard = json.dumps({'keyboard': [["/ayuda"], ["/crear"]], 'one_time_keyboard': True, 'resize_keyboard': True})
option2_keyboard = json.dumps({'keyboard': [["/guardar"],["/no_guardar"]], 'one_time_keyboard': True, 'resize_keyboard': True})
option3_keyboard = json.dumps({'keyboard': [["/borrar"],["/seguir"]], 'one_time_keyboard': True, 'resize_keyboard': True})
#a = Value('i', 4)

def checkFile(file_tofill):
    return os.path.isfile(str(file_tofill))

def fileIsEmpty(path):
    return os.path.getsize(path) <=1

def fillVariables(new):
    list = ""
    modifier = ""
    for i in new:
        if i != new[0]:
            list += i + " "
        else:
            modifier = modifier + i
            modifier = modifier.replace(modifier[0], "")
    list = list[:-1]
    return list, modifier

def fileList(path, username):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if username in file:
                files.append(os.path.join(r,file))
    return files

def deleteFiles(ufile):
    for i in ufile:
        os.remove(i)

def obtainSecretBook(file):
    for i in allobjects.objectLibros:
        if "RoddyLibro" in i["objeto"]:
            if inv.checkObject(str(file), i["objeto"]) == False:
                inv.addtoInventory(str(file), i["objeto"], i["descripcion"], i["tipo"])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.text == "/start":
        	bot.send_message(message.chat.id, """Bienvenido a roddyBot!!\n\nUn bot en el que vivirás miles de aventuras!""", reply_markup = menu_keyboard)
    elif message.text == "/help":
        bot.send_message(message.chat.id, """Lista de comandos!!
        \n\n/start - Te permite iniciar el bot\n\n/help - Muestra los comandos posibles
        \n\n/crear_personaje - Te permite entrar en el menú de creación de personaje
        \n\n/armas - Muestra todas las armas que puedo darte... ¡Ten cuidado son peligrosas!
        \n\n/armaduras - Muestra todas las armaduras que puedo darte. ¡Una buena defensa siempre ayuda!
        \n\n/coleccionables - Muestra todos los objetos especiales que existen!
        \n\n/libros - Muestra todos los libros que existen, ¡Encuentralos todos!
        \n\n/yo - Permite revisar tú personaje
        \n\n/inv - Permite revisar tu inventario
        \n\n/equipar [nombre arma o armadura] - Permite equiparte armas y armaduras!""")

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
        \n\n/apariencia [pequeña descripción o link a una imagen] \n\nejemplo: /apariencia azul | /apariencia http://cosas.imagen/imagen.jpg
        \n\n/personalidad [describir personalidad]
        \n\n/histroria [pequeña historia de tu personaje]
        \n\n/estatus para comprovar que campos faltan o para guardar el personaje""")
        create_character(message)

    elif message.text =="/crear":
        username = "characters/" + message.chat.first_name

        if checkFile(str(username)+"_pj.txt") == True:
            bot.send_message(message.chat.id, "Ya tienes un personaje. ¿Quieres borrar tu personaje?", reply_markup = option3_keyboard)
        else:
            pj.createPjDict(str(message.chat.id))
            bot.send_message(message.chat.id,"""Iniciando proceso de creación de personaje. \nPor favor usa /estatus para revisar que campos faltan por crear.""")
            documentoPj = open (str(username) + "_pj.txt", "w+")
            documentoPj.write("nombre ; edad ; clase ; apariencia ; personalidad ; historia" + "\n")
            documentoPj.close()
            documentoPj = open (str(username) + "_inv.txt", "w+")
            documentoPj.write("objeto ; descripción ; tipo" + "\n")
            documentoPj.close()

@bot.message_handler(commands=['nombre','edad', 'clase', 'apariencia','personalidad','historia'])
def addNameChar(message):
    if pj.cidExists(str(message.chat.id)) == False:
        bot.send_message(message.chat.id, "No puedes editar directarmente.\n\nPon /crear_personaje o si ya tienes uno, borralo tras entrar de nuevo en el menú de creación.")
    else:
        new = message.text.split()
        if len(new) == 1:
            bot.send_message(message.chat.id, "No entiendo que quieres añadir, por favor despues del comando añade un parámetro.\n\nEjemplo: /nombre Paco Fernandez.")
        else:
            show, definer = fillVariables(new)
            pj.addField(str(message.chat.id), definer, show)
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
                bot.send_message(message.chat.id,"Veo que tienes una historia... Algún día te contaré mi_historia, amigo.")


@bot.message_handler(commands=['estatus'])
def creationStatus(message):
    missingElements = pj.charCheck(str(message.chat.id))
    if len(missingElements) >= 1:
        bot.send_message(message.chat.id, "Faltan los siguientes campos por rellenar: " + str(missingElements) + ".")
    else:
        bot.send_message(message.chat.id, "¡Todos los campos creados! ¿Quieres guardar los cambios en tu fichero de personaje?", reply_markup = option2_keyboard)

@bot.message_handler(commands=['guardar','no_guardar'])
def saveCharValues(message):
    if message.text == "/guardar":
        charFile = "characters/" + str(message.chat.first_name) + "_pj"
        invFile = "characters/" + str(message.chat.first_name) + "_inv.txt"
        eqFile = "characters/" + str(message.chat.first_name) + "_eq.txt"
        if checkFile(str(charFile) + ".txt") == True:
            pj.saveCharVal(str(charFile), str(message.chat.id))
        else:
            documentoPj = open (str(charFile) + ".txt", 'w+')
            documentoPj.write("nombre ; edad ; clase ; apariencia ; personalidad ; historia" + "\n")
            documentoPj.close()
            pj.saveCharVal(str(charFile), str(message.chat.id))
        bot.send_message(message.chat.id, "Personaje creado, ahora será añadido tu inventario.")
        if checkFile(str(invFile)) == True:
            inv.addtoInventory(invFile, allobjects.objectArmas[0]["objeto"],allobjects.objectArmas[0]["descripcion"],allobjects.objectArmas[0]["tipo"])
            inv.addtoInventory(invFile, allobjects.objectArmaduras[0]["objeto"],allobjects.objectArmaduras[0]["descripcion"],allobjects.objectArmaduras[0]["tipo"])
            inv.addtoInventory(invFile, allobjects.objectColeccionables[0]["objeto"],allobjects.objectColeccionables[0]["descripcion"],allobjects.objectColeccionables[0]["tipo"])
        bot.send_message(message.chat.id, "¡Listo!\n\nPuedes mirar tu personaje con /yo\n\nTu inventario con /inv o /inventario\n\nFinalmente puedes /equipar [nombre arma] o /equipar [nombre armadura]\n\n IMPORTANTE: Revisa el inventario cada vez que quieras equipar algo, ya que se requiere el nombre completo.")
    else:
        pj.removeAllFields(str(message.chat.id))

@bot.message_handler(commands=['armas','libros','armaduras','coleccionables'])
def showArmas(message):
    string = ""
    if "/armas" in message.text:
        string = "Armas\n--------------------------------------------------\n"
        for i in allobjects.objectArmas:
            string += i["objeto"]+":" + i["descripcion"] + i["tipo"] + "\n\n"
    if "/libros" in message.text:
        string = "Libros\n--------------------------------------------------\n"
        for i in allobjects.objectLibros:
            string += i["objeto"]+":" + i["descripcion"] + i["tipo"] + "\n\n"
    if "/armaduras" in message.text:
        string = "Armaduras\n--------------------------------------------------\n"
        for i in allobjects.objectArmaduras:
            string += i["objeto"]+":" + i["descripcion"] + i["tipo"] + "\n\n"
    if "/coleccionables" in message.text:
        string = "Coleccionables\n--------------------------------------------------\n"
        for i in allobjects.objectColeccionables:
            string += i["objeto"]+":" + i["descripcion"] + i["tipo"] + "\n\n"
    bot.send_message(message.chat.id, str(string))

@bot.message_handler(commands=['yo'])
def mostraPersonatge(message):
    charFile = "characters/" + str(message.chat.first_name) + "_pj"
    content = pj.checkFileContent(str(charFile)+".txt")
    bot.send_message(message.chat.id, "Mostrando tu personaje:\n\n -------------------------------------- \nnombre: " + str(content[0]) + "\nedad: " + str(content[1]) + "\nclase: " + str(content[2]) + "\napariencia: " + str(content[3]) + "\npersonalidad: " + str(content[4]) + "\nhistoria: " + str(content[5]))


@bot.message_handler(commands=['inventario','inv'])
def mostraInv(message):
    invFile = "characters/" + str(message.chat.first_name) + "_inv"
    invContent = inv.showInv(invFile+".txt")
    string = "Objetos\n--------------------------------------------------\n"
    for i in invContent:
        string += i["objeto"]+":" + i["descripcion"] + i["tipo"]+"\n"
    bot.send_message(message.chat.id, str(string))

@bot.message_handler(commands=['equipar'])
def equipar(message):
    userfile = "characters/"+str(message.chat.first_name)+"_inv.txt"
    if equip.checkCid(str(message.chat.id)) == False:
        equip.createEqDict(str(message.chat.id))
    missingElements = []
    new = message.text.split()
    show, definer = fillVariables(new)

    if inv.checkObject(str(userfile), show) == True:
        if "[Arma]" in inv.checkType(str(userfile), show):
            equip.addField(str(message.chat.id), "arma", show)
            missingElements = equip.checkFields(str(message.chat.id))
            bot.send_message(message.chat.id,"Arma Equipada!")
            if len(missingElements)>0:
                bot.send_message(message.chat.id,"Falta por añadir: " + str(missingElements))
            else:
                bot.send_message(message.chat.id,"Usa /equipo para que los cambios sean guardados")
        elif "[Armadura]" in inv.checkType(str(userfile), show):
            equip.addField(str(message.chat.id), "armadura", show)
            missingElements = equip.checkFields(str(message.chat.id))
            bot.send_message(message.chat.id,"Armadura Equipada!")
            if len(missingElements)>0:
                bot.send_message(message.chat.id,"Falta por añadir: " + str(missingElements))
            else:
                bot.send_message(message.chat.id,"Usa /equipo para que los cambios sean guardados")
        else:
            bot.send_message(message.chat.id, "¡Eso no es ni un Arma ni una Armadura!")
    else:
        bot.send_message(message.chat.id,"No puedo equiparte un objeto que no tienes.")

@bot.message_handler(commands=['equipo'])
def mostrarEq(message):
    eqFile = "characters/"+str(message.chat.first_name)+"_eq.txt"
    string = ""
    if equip.checkCid(str(message.chat.id)) == True:
        eqDict = equip.showEq(str(message.chat.id))
        for key, value in eqDict.items():
            if key != "cid":
                string += key+": " + value + "\n"
        fileEq = open(eqFile,'w')
        fileEq.write(string)
        fileEq.close()
        bot.send_message(message.chat.id,"Equipo actual.\n--------------------------------------\n"+ str(string))
    elif checkFile(eqFile) == True:
        if fileIsEmpty(eqFile) == True:
            bot.send_message(message.chat.id, "Deberias probar a equiparte algo antes de mirar que equipo tienes...")
        else:
            fileEq = open(eqFile,'r')
            doc_contents = fileEq.readlines()
            for i in doc_contents:
                string += i
            bot.send_message(message.chat.id,"Equipo actual.\n--------------------------------------\n"+ str(string))
    else:
        bot.send_message(message.chat.id, "Deberias probar a equiparte algo antes de mirar que equipo tienes...")

@bot.message_handler(commands=['borrar','seguir'])
def borrarPJ(message):
    if message.text == "/borrar":
        ufiles = fileList("characters/", str(message.chat.first_name))
        if not ufiles:
            bot.send_message(message.chat.id,"¡Y-ya basta!¿No ves que ya está borrado? QwQ\n\n Crea un personaje desde /crear_personaje")
        else:
            deleteFiles(ufiles)
            bot.send_message(message.chat.id,"Personaje Borrado!\n\nAhora serás redireccionado al menú de creación.")
            create_character(message)
    else:
        bot.send_message(message.chat.id,"Has escogido seguir con tu personaje, estoy orgulloso de ti.")

@bot.message_handler(commands=['leer'])
def readBook(message):
    file = "characters/"+str(message.chat.first_name)+"_inv.txt"
    new = message.text.split()
    show, definer = fillVariables(new)
    if inv.checkObject(str(file),show) == True:
        if "[Libro]" in inv.checkType(str(file), show):
            bot.send_message(message.chat.id, "Accediendo al contenido del libro...")
            read = book.readBooks(str(show))
            time.sleep(5)
            bot.send_message(message.chat.id, str(read))
        else:
            bot.send_message(message.chat.id, "Creo que " +str(show)+" no es un libro, o quizás es que es un item que no tienes. De cualquier modo, lo siento, prueba a escribir el nombre de un libro que tengas por favor...")
    else:
        bot.send_message(message.chat.id, "No puedo mostrarte algo que no tienes.")

@bot.message_handler(commands=['mi_historia'])
def botHistoria(message):
    file = "characters/"+message.chat.first_name+"_inv.txt"
    bot.send_message(message.chat.id, "Así que quieres saber mi historia... Gracias.")
    obtainSecretBook(file)
    bot.send_message(message.chat.id, "Creo que deberías revisar tu inventario. Aunque quizás ya lo tenías.")

bot.polling(none_stop=True)
