from telethon import TelegramClient, events
from time import sleep
from text import *

#.stringify()

try:
    with open('config.ini', "r") as file:
        for line in file:
            if line == "[spambot]":
                continue
            if line == "[\\spambot]":
                break
            if line.startswith("api_id="):
                api_id = line.replace("api_id= ", "").replace("\n", "")
            elif line.startswith("api_hash="):
                api_hash = line.replace("api_hash= ", "").replace("\n", "")
            elif line.startswith("phon_num="):
                phone = line.replace("phon_num= ", "").replace("\n", "")
            
except FileNotFoundError:
    with open('config.ini', "w") as file:
        in_api_id = input("Ведите свой api_id:")
        in_api_hash = input("Ведите свой api_hash:")
        in_api_phone = input("Ведите свой номер телефона(с префиксом страны и +):")
        file.write(f"[spambot]\napi_id= {in_api_id}\napi_hash= {in_api_hash}\nphon_num= {in_api_phone}\n[\\spambot]")
        api_id = in_api_id
        api_hash = in_api_hash
        phone = in_api_phone

client = TelegramClient('spam_bot', api_id, api_hash)
client.start(phone=phone)

@client.on(events.NewMessage(pattern=".info"))
async def info(event):
    print(event.stringify())   

@client.on(events.NewMessage(pattern=".spam"))
async def spam(event):
    num = 0
    a = event.message.message.split(" ")
    text = str(event.message.message).replace(f".spam {a[1]}", "")
    while int(a[1]) != num:
        await client.send_message(event.chat_id, text)
        num += 1

@client.on(events.NewMessage(pattern=".help"))
async def help(event):
    await client.edit_message(event.chat_id, event.message.id, help_text)
    
@client.on(events.NewMessage(pattern=".gul"))
async def gul(event):
    n = 1000
    await client.edit_message(event.chat_id, event.message.id, "Я гуль")
    await client.send_message(event.chat_id, f"{n} - 7")
    while n != -1:
        n -= 7
        if n == -1:
            await client.send_message(event.chat_id, f"-1")
            await client.send_message(event.chat_id, f"Гуль обнаружен")
        else:
            await client.send_message(event.chat_id, f"{n} - 7")

@client.on(events.NewMessage(pattern=".type"))    
async def type(event):
	orig_text = event.message.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = ''
	typing_symbol = "¶"

	while(tbp != orig_text):
		await client.edit_message(event.chat_id, event.message.id, tbp + typing_symbol)
		sleep(0.05)
		tbp = tbp + text[0]
		text = text[1:]
		await client.edit_message(event.chat_id, event.message.id, tbp)
		sleep(0.05)
    
@client.on(events.NewMessage(pattern=".love"))
async def love(event):
    await client.edit_message(event.chat_id, event.message.id, heart_ani_11)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_10)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_9)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_8)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_7)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_6)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_5)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_4)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_3)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_2)
    await client.edit_message(event.chat_id, event.message.id, heart_ani())
    await client.edit_message(event.chat_id, event.message.id, heart_ani())
    await client.edit_message(event.chat_id, event.message.id, heart_ani())
    await client.edit_message(event.chat_id, event.message.id, heart_ani())
    await client.edit_message(event.chat_id, event.message.id, heart_ani())
    await client.edit_message(event.chat_id, event.message.id, heart_ani())
    await client.edit_message(event.chat_id, event.message.id, heart_ani())
    await client.edit_message(event.chat_id, event.message.id, heart_ani())
    await client.edit_message(event.chat_id, event.message.id, heart_ani())
    await client.edit_message(event.chat_id, event.message.id, heart_ani_2)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_3)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_4)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_5)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_6)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_7)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_8)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_9)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_10)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_11)
    await client.edit_message(event.chat_id, event.message.id, heart_ani_12)

client.run_until_disconnected()