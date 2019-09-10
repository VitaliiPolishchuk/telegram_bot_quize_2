from random import randint
from config import shelve_name
import string_variables

def get_exit_message():
    return string_variables.exit_message

def get_top_users():
    return string_variables.top_users

def get_list_users_button():
    return string_variables.list_users_button

def get_start_cheering_button():
	return string_variables.start_cheering_button

def get_only_one_time_game():
    return string_variables.only_one_time_game

def get_hello():
    return string_variables.hello

def get_final_message():
    return string_variables.final_message

def get_praise(time):
	if time == 2:
		return string_variables.praises[0]
	elif time == 3:
		return string_variables.praises[1]
	elif time == 6:
		return string_variables.praises[2]
	elif time == 11:
		return string_variables.praises[3]
	elif time == 14:
		return string_variables.praises[4]

def get_yes_button():
	return string_variables.yes_button

def get_no_button():
	return string_variables.no_button

def get_ask_feedback():
	return string_variables.ask_feedback

def get_result_message():
	return string_variables.result_message

def get_juremix_love():
	return string_variables.juremix_love

def get_cheering_message():
	return string_variables.cheering_message

def get_delete_data_button():
	return string_variables.delete_data_button

def get_pass_one_time():
	return string_variables.pass_one_time

def get_instructions():
	return string_variables.instructions