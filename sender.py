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

	client = TelegramClient('session_name_1', api_id, api_hash)
	client.start()
	return client

message = emoji.emojize('Привет! Давай поиграем!😊\nЧтобы начать, переходи по ссылке:down_arrow::winking_face:\n\n@jurimex_bot')
# client = get_client()

def send_messages(client):
	db_worker = SQLither(config.database_name)
	users = db_worker.select_all_real_users()
	for user in users:
		print("{} {}".format(user.get_phone(), user.get_initials()))
		client.send_message(user.get_phone(), message)
	db_worker.close()

# client.send_message('+380989586177', message)

# result = client(functions.contacts.GetContactsRequest(hash=api_id))
# print(len(result.users))
# for user in result.users:

# send_messages(client)

send_messages(get_client())