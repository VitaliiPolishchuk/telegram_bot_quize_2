import logging

from SQLither import *
import string_worker, utils
from UserData import UserData
import time
from random import randint
import Questions
from aiogram import Bot, Dispatcher, executor, types
import config
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage


logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=config.token)
dp = Dispatcher(bot)
time_await = 5	


async def start_cheering_real_users():
	while True:
		db_worker = SQLither(config.database_name)
		users = db_worker.select_real_users_in_bot()
		for user in users:
			print(int(user.get_last_activity()))
			if int(user.get_last_activity()) + 3600 < time.time():
				await send_message(user.get_user_id(), string_worker.get_cheering_message())
				db_worker.update_last_activity(user.get_user_id(), time.time())
		db_worker.close()
		await asyncio.sleep(600)

async def send_message(chat_id, text, delay=0, parse_mode=None, reply_markup=None):
	await bot.send_chat_action(chat_id, 'typing')
	await asyncio.sleep(time_await)
	await bot.send_message(chat_id, text, parse_mode=parse_mode, reply_markup=reply_markup)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):

	print("{} has id {}".format(message.chat.username, message.chat.id))

	# for question in Questions.questions:
	# 	await send_message(message.chat.id, question, parse_mode='HTML')

	if message.chat.id in config.admins:
		markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)	
		markup.add(string_worker.get_list_users_button())
		# markup.add(string_worker.get_delete_data_button())

		await send_message(message.chat.id, string_worker.get_instructions(), parse_mode='HTML', reply_markup=markup)

		return 
	else:
		# user_data = UserData(message.chat.id)
		# user_data.delete()
		user_data = UserData(message.chat.id)
		user_data.set_is_active(True)
		user_data.save()
		db_worker = SQLither(config.database_name)
		if db_worker.is_user_exist(message.chat.id):
			await send_message(message.chat.id, string_worker.get_pass_one_time())
			return 
		else:
			db_worker.update_last_activity(message.chat.id, time.time())
			db_worker.insert_user(message.chat.id, message.chat.first_name, message.chat.last_name, message.chat.username)
		db_worker.close()

		markup = types.ReplyKeyboardRemove()

		await send_message(message.chat.id, string_worker.get_hello(), parse_mode='HTML', reply_markup=markup)

		await asyncio.sleep(10)
		await bot.send_chat_action(message.chat.id, 'upload_video')
		await asyncio.sleep(5)
		await bot.send_video(message.chat.id, config.pic_begin_game)

		await asyncio.sleep(5)

		next_question_id = Questions.get_next_random_question_id(user_data.get_answers_id())
		user_data.set_question_id(next_question_id)
		question_text = Questions.get_question(next_question_id)
		await send_message(message.chat.id, "<b>{}.</b> {}".format(user_data.get_count_answers(), question_text), parse_mode='HTML')
		user_data.set_is_active(False)
		user_data.save()

	

def get_file_id(message):
	return message['video']['file_id']

@dp.message_handler(content_types=["video"])
async def send_video_to_real_users(message: types.Message):
	print("{} has id has send video".format(message.chat.username))
	db_worker = SQLither(config.database_name)
	users = db_worker.select_all_real_users()
	db_worker.close()
	for user in users:
		print(user.get_user_id())
		try:
			await send_message(user.get_user_id(), string_worker.get_juremix_love())
			await bot.send_video(user.get_user_id(), get_file_id(message))
		except:
			print("{} not in bot".format(user.get_user_id()))
	await send_message(message.chat.id, 'Я прислал видео')
	
@dp.message_handler()
async def handle_main_menu_input(message: types.Message):
	if not message.chat.id in config.admins:
		user_data = UserData(message.chat.id)
		if user_data.is_active:
			return 
		user_data.set_is_active(True)
		user_data.save()
		if message.text == string_worker.get_yes_button() or message.text == string_worker.get_no_button():
			feedback = 0
			if message.text == string_worker.get_yes_button():
				feedback = 1
			db_worker = SQLither(config.database_name)
			db_worker.insert_feedback(message.chat.id, feedback)
			db_worker.close()
			print("{} set {} feedback".format(message.chat.username, feedback))
			user_data.set_question_id(-1)
			user_data.save()
			await send_message(message.chat.id, string_worker.get_result_message(), reply_markup=types.ReplyKeyboardRemove())
			await result(message)
		else:
			await play_game(message)
		user_data = UserData(message.chat.id)
		user_data.set_is_active(False)
		user_data.save()
	else:
		if message.text == string_worker.get_list_users_button():
			db_worker = SQLither(config.database_name)
			utils.generate_list_users(db_worker)
			db_worker.close()
			await bot.send_document(message.chat.id, open(config.users_file, 'rb'))
		# elif message.text == string_worker.get_delete_data_button():

		# 	db_worker = SQLither(config.database_name)
		# 	users = db_worker.select_real_users_in_bot()
		# 	for user in users:
		# 		user_data = UserData(user.get_user_id())
		# 		user_data.delete()
		# 	db_worker.delete_all_data()
		# 	db_worker.close()
		# 	await send_message(message.chat.id, 'Данные удалено')
		elif message.text == 'Start cheering users :)':
			await start_cheering_real_users()



async def play_game(message):
    print("{} play game".format(message.chat.username))
    user_data = UserData(message.chat.id)
    print(user_data.get_count_answers())
    if user_data.get_count_answers() != 0:
        db_worker = SQLither(config.database_name)
        db_worker.insert_answer(message.chat.id, user_data.get_question_id(), message.text)
        db_worker.update_last_activity(message.chat.id, time.time())
        db_worker.close()	

    if user_data.get_count_answers() > Questions.get_questions_limit():
    	return

    if user_data.get_count_answers() == Questions.get_questions_limit():
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
        markup.add(string_worker.get_yes_button())
        markup.add(string_worker.get_no_button())
        await send_message(message.chat.id, string_worker.get_ask_feedback(), reply_markup=markup)
        db_worker = SQLither(config.database_name)
        db_worker.update_last_activity(message.chat.id, time.time() + 10000000)
        db_worker.close()
        return 

    next_question_id = Questions.get_next_random_question_id(user_data.get_answers_id())
    user_data.set_question_id(next_question_id)
    question_text = Questions.get_question(next_question_id)
    if Questions.is_time_to_praise(user_data.get_count_answers()):
        await send_message(message.chat.id, string_worker.get_praise(user_data.get_count_answers()), parse_mode='HTML')
    user_data.save()
    await send_message(message.chat.id, "<b>{}.</b> {}".format(user_data.get_count_answers(), question_text), parse_mode='HTML')

    
    

    
async def result(message):
	print("{} get results".format(message.chat.username))
	# await send_message(message.chat.id, string_worker.get_final_message())
	await asyncio.sleep(5)
	await bot.send_chat_action(message.chat.id, 'upload_video')
	await asyncio.sleep(5)
	await bot.send_video(message.chat.id, config.pic_final)



if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)