
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
from requests import HTTPError
from time import sleep
import requests
import random

heart = ['💙', '💚', '❤️', '💜', '🧡', '💛']

commands = """
.spam 1 2 - Где 1 это число отправлений, а 2 это текст (Обычная отправка сообщений с указаным текстом)
.spamg 1 - 1 это число отправлений, должна быть ответом на гифку (спамит гифками)
.spams 1 - 1 это число отправлений, должна быть ответом на стикер (спамит стикерами)
.type 2 - 2 это текст (Красиво печатает текст)
.love - анимация сердечка (Как найду автора идеи отмечу его тут)
"""

heart_ani_1 = f"""
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍🖤🖤🖤🤍
🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤
🤍🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍
🤍🤍🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍🤍
🤍🤍🤍🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍🤍🤍
🤍🤍🤍🤍🤍🤍🖤{random.choice(heart)}🖤🤍🤍🤍🤍
"""
heart_ani_2 = f"""
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍🖤🖤🖤
🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤
🤍🤍🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍
🤍🤍🤍🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍🤍
"""
heart_ani_3 = f"""
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍🖤🖤
🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍🖤{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🤍🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤
"""
heart_ani_4 = f"""
🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍🖤
🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍🖤{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
"""
heart_ani_5 = f"""
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍🖤
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
"""
heart_ani_6 = f"""
🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍
🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
"""
heart_ani_7 = f"""
🤍🤍🤍🤍🤍🤍
🤍🤍🤍🖤🖤🖤
🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}
"""
heart_ani_8 = f"""
🤍🤍🤍🤍
🤍🤍🤍🖤
🤍🤍🖤{random.choice(heart)}{random.choice(heart)}
🤍🖤{random.choice(heart)}{random.choice(heart)}
"""
heart_ani_9 = f"""
🤍🤍🤍
🤍🤍🤍
🤍🤍🖤
"""
heart_ani_10 = f"""
🤍🤍
🤍🤍
"""
heart_ani_11 = f"""
🤍⠀
"""
heart_ani_12 = f"""
🤍 I love you!
"""

		
app = Client('my_account')

@app.on_message(filters.me & filters.command('help', prefixes = ['.']))
def help(client, message):
	app.edit_message_text(message.chat.id, message.message_id, commands)


@app.on_message(filters.me & filters.command('info', prefixes = ['.']))
def info(client, message):
	print (message)

@app.on_message(filters.me & filters.command('kick', prefixes = ['.']))
def kick(client, message):
	er = message.user.first_name, " Выгнал: " + message.reply_to_message.from_user.first_name
	app.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
	message.edit(text = er )


@app.on_message(filters.me & filters.command('unban', prefixes = ['.']))
def unban(client, message):
	pass



@app.on_message(filters.me & filters.command('block', prefixes = ['.']))
def bl(client, message):
	pass


@app.on_message(filters.me & filters.command('unblock', prefixes = ['.']))
def unbl(client, message):
	pass


@app.on_message(filters.me & filters.command('spamg', prefixes =['.']) & filters.reply )
def spamg(client, message):
	coun = 0
	cou = message.command[1]
	print(cou)
	try:
		while(int(coun) != int(cou)):
			coun = coun + 1
			app.send_animation(message.chat.id, message.reply_to_message.animation.file_id)

	except FloodWait as e:
			sleep(e.x)	

@app.on_message(filters.me & filters.reply & filters.command('spams', prefixes =['.']))
def spams(client, message):
	coun = 0
	cou = message.command[1]
	try:
		while(int(coun) != int(cou)):
			coun = coun + 1
			app.send_sticker(message.chat.id, message.reply_to_message.sticker.file_id)

	except FloodWait as e:
			sleep(e.x)

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

		except FloodWait as e:
			sleep(e.x)

@app.on_message(filters.me & filters.command('love', prefixes = ['.']))
def love(client, message):
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_11)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_10)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_9)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_8)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_7)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_6)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_5)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_4)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_3)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_2)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_1)
	s = 0
	while s != 10:
		heart_2 = f"""
🤍🤍🖤🖤🖤🤍🤍🤍🖤🖤🖤🤍🤍
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍
🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤
🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤
🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤
🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍
🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍🤍
🤍🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍🤍🤍
🤍🤍🤍🤍🖤{random.choice(heart)}{random.choice(heart)}{random.choice(heart)}🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🖤{random.choice(heart)}🖤🤍🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🖤🤍🤍🤍🤍🤍🤍
"""
		app.edit_message_text(message.chat.id, message.message_id, heart_2)
		s = s + 1
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_1)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_2)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_3)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_4)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_5)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_6)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_7)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_8)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_9)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_10)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_11)
	app.edit_message_text(message.chat.id, message.message_id, heart_ani_12)

app.run()