try:
	file = open("config.ini", "r")
	print(file.read())
	file.close()
except FileNotFoundError:
	file = open("config.ini", "w")
	print("api_id:")
	id = input()
	print("api_hash:")
	hash = input("")
	file.write("[pyrogram]\napi_id = "+id+"\napi_hash = "+hash)
	file.close()
