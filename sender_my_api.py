from telethon import TelegramClient, events, sync
from telethon.tl.functions.users import GetFullUserRequest
import config
from SQLither import *
import asyncio
import random
import emoji
from telethon import functions, types

api_id = 
api_hash = 

def get_client():

	client = TelegramClient('session_name', api_id, api_hash)
	client.start()
	return client

message = emoji.emojize('Бажаю вам чудового настрою і приємного дня!')
client = get_client()

# def send_messages(client):
# 	db_worker = SQLither(config.database_name)
# 	users = db_worker.select_all_real_users()
# 	for user in users:
# 		print("{} {}".format(user.get_phone(), user.get_initials()))
# 		client.send_message(user.get_phone(), message)
# 	db_worker.close()

result = client(functions.contacts.GetContactsRequest(hash=api_id))
for user in result.users:
	print("+{}".format(user.phone))
	client.send_message("+{}".format(user.phone), message)

# client.send_message('+380683221354', message)

# send_messages(client)

# send_messages(get_client())