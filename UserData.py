# -- coding utf-8 --
import sqlite3
import shelves_handler
import time, datetime

class UserData:

    def __init__(self, chat_id):
        json = shelves_handler.get_user_data(chat_id)
        self.chat_id = chat_id
        if not json: 
            self.question_id = 0
            self.answers = set()
            self.is_active = True
        else:
            self.question_id = json['question_id']
            self.answers = json['answers']
            self.is_active = json['is_active']

    def save(self):
        json = {}
        json['chat_id'] = self.chat_id
        json['question_id'] = self.question_id
        json['answers'] = self.answers
        json['is_active'] = self.is_active
        shelves_handler.save_user_data(self.chat_id, json)

    def delete(self):
        shelves_handler.delete_user_data(self.chat_id)

    def get_question_id(self):
        return self.question_id

    def set_question_id(self, question_id):
        self.question_id = question_id
        self.answers.add(question_id)

    def get_count_answers(self):
        return len(self.answers)

    def get_answers_id(self):
        return self.answers

    def is_active(self):
    	return self.is_active

    def set_is_active(self, value):
    	self.is_active = value
