
try:
	file = open("config.ini", "r")
	print(file.read())
	file.close()
except FileNotFoundError:
	file = open("config.ini", "w")
	print("api_id:")
	id = input()
	print("api_hash:")
	hash = input()
	file.write("[pyrogram]\napi_id = "+id+"\napi_hash = "+hash)
	file.close()

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
import requests
		
app = Client('my_account')

@app.on_message(filters.command("in", prefixes="."))
def info(client, message):
	print (message)

@app.on_message(filters.me& filters.command('spamg', prefixes =['.']) & filters.reply )
def spamg(client, message):
	coun = 0
	cou = message.command[1]
	print(cou)
	try:
		while(int(coun) != int(cou)):
			coun = coun + 1
			app.send_animation(message.chat.id, message.reply_to_message.animation.file_id)
	

@app.on_message(filters.me & filters.reply & filters.command('spams', prefixes =['.']))
def spams(client, message):
	coun = 0
	cou = message.command[1]
	try:
		while(int(coun) != int(cou)):
			coun = coun + 1
			app.send_sticker(message.chat.id, message.reply_to_message.sticker.file_id)


@app.on_message(filters.me & filters.command('spam', prefixes =['.']))
def spam(client, message):
	coun = 0
	cou = message.command[1]
	orig_text = message.text.split(".spam ", maxsplit=1)[1]#Убираем из полученого текста команду
	text = message.command[2:]
	text_p = str(text).replace('[', '').replace(']', '').replace("'", '').replace(",", '')
	while(int(coun) != int(cou)):
		coun = coun + 1
		app.send_message(message.chat.id, text_p)

@app.on_message(filters.me & filters.command('type', prefixes =['.']))#Задаем филтер чтоб принимал только сообщение клиента и филтрацию на команду
def type(client, message):
	orig_text = message.text.split(".type ", maxsplit=1)[1]#Убираем из полученого текста команду
	text = orig_text
	tbp = ''
	typing_symbol = "¶"#Символ для пичатанья

	while(tbp != orig_text):
		#повторяем пока tbp е будет равно оригинальному тексту
		try:
			message.edit(tbp + typing_symbol)
			sleep(0.05)

			tbp = tbp + text[0]
			text = text[1:]

			message.edit(tbp)
			sleep(0.05)




app.run()
