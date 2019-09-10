# -- coding utf-8 --
import sqlite3
from UserDataDB import UserDataDB
from RealUserDataDB import RealUserDataDB
from RealUserDataToExcel import RealUserDataToExcel
from RealUserExcelData import RealUserExcelData
from UsersFeedbackData import UsersFeedbackData
from Answers import Answers

class SQLither:


    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        with self.connection:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS answers (user_id INTEGER, question_id INTEGER, answer_text TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS users (Id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, user_name TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS last_activities (user_id INTEGER, unix_time INTEGER)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS non_exist_users (initials TEXT, phone TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS real_users (Id INTEGER, initials TEXT, phone TEXT)')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS feedbacks (user_id INTEGER, feedback INTEGER)')
        self.connection.commit()

    def insert_answer(self, user_id, question_id, answer):
        with self.connection:
            self.cursor.execute('INSERT INTO answers VALUES(?,?,?)', (user_id, question_id, answer))

    def insert_user(self, user_id, first_name, last_name, user_name):
        with self.connection:
            self.cursor.execute('INSERT INTO users VALUES(?,?,?,?)', (user_id,first_name,last_name,user_name)).fetchall()

    def is_user_exist(self, user_id):
        with self.connection:
            return len(self.cursor.execute('SELECT * FROM users WHERE Id = ?', (user_id,)).fetchall()) == 1

    def update_last_activity(self, user_id, time):
        with self.connection:
            if len(self.cursor.execute('SELECT * FROM last_activities WHERE user_id = ?', (user_id,)).fetchall()) == 1:
                self.cursor.execute('UPDATE last_activities SET unix_time = ? WHERE user_id = ?', (time, user_id))
            else:
                self.cursor.execute('INSERT INTO last_activities VALUES(?, ?)', (user_id, time))

    def select_all_answers_by_user(self, user_id):
        with self.connection:
            result = []
            for row in self.cursor.execute('SELECT question_id, answer_text FROM answers WHERE user_id = ?', (user_id, )).fetchall():
                result.append(Answers(row[0], row[1]))
            return result

    def select_all_users(self):
        with self.connection:
            result = []
            for row in self.cursor.execute('SELECT Id, first_name, last_name, user_name, last_activities.unix_time FROM users INNER JOIN last_activities ON users.Id = last_activities.user_id').fetchall():
                result.append(UserDataDB(row[0], row[1], row[2], row[3], row[4]))
            return result

    def select_all_real_users_to_excel(self):
        with self.connection:
            result = []
            for row in self.cursor.execute('SELECT Id, initials, phone, last_activities.unix_time FROM real_users INNER JOIN last_activities ON real_users.Id = last_activities.user_id').fetchall():
                result.append(RealUserDataToExcel(row[0], row[1], row[2], row[3]))
            return result

    def select_all_users_feedbacks(self):
        with self.connection:
            result = []
            for row in self.cursor.execute('SELECT Id, initials, phone, feedbacks.feedback FROM real_users INNER JOIN feedbacks ON real_users.Id = feedbacks.user_id').fetchall():
                result.append(UsersFeedbackData(row[0], row[1], row[2], int(row[3])))
            return result

    def select_all_real_users(self):
        with self.connection:
            result = []
            for row in self.cursor.execute('SELECT * FROM real_users').fetchall():
                result.append(RealUserDataDB(row[0], row[1], row[2]))
            return result

    def insert_non_exist_user(self, initials, phone):
        with self.connection:
            # if self.cursor.execute('SELECT * FROM non_exist_users WHERE phone = ?', (phone, )).fetchall() == 0:
            self.cursor.execute('INSERT INTO non_exist_users VALUES(?,?)', (initials, phone)).fetchall()

    def insert_real_user(self, user_id, initials, phone):
        with self.connection:
            # if self.cursor.execute('SELECT * FROM real_users WHERE Id = ?', (user_id,)).fetchall() == 0:
            self.cursor.execute('INSERT INTO real_users VALUES(?,?,?)', (user_id, initials, phone)).fetchall()

    def select_all(self):
        with self.connection:
            return self.cursor.execute('SELECT * FROM questions').fetchall()

    def select_all_answers(self):
        with self.connection:
            result = []
            for row in self.cursor.execute('SELECT * FROM category_answer').fetchall():
                result.append(row[1])
            return result

    def select_all_users_not_in_bot(self):
        with self.connection:
            result = []
            for row in self.cursor.execute('SELECT * FROM real_users WHERE Id NOT IN (SELECT Id FROM users)').fetchall():
                result.append(RealUserDataDB(row[0], row[1], row[2]))
            return result

    def select_all_users_not_exist(self):
        with self.connection:
            result = []
            for row in self.cursor.execute('SELECT * FROM non_exist_users').fetchall():
                result.append(RealUserExcelData(row[0], row[1]))
            return result

    def insert_feedback(self, user_id, feedback):
        with self.connection:
            self.cursor.execute('INSERT INTO feedbacks VALUES(?,?)', (user_id, feedback)).fetchall()

    def select_real_users_in_bot(self):
        with self.connection:
            result = []
            for row in self.cursor.execute('SELECT Id, initials, phone, last_activities.unix_time FROM real_users INNER JOIN last_activities ON real_users.Id = last_activities.user_id WHERE real_users.Id IN (SELECT Id FROM users)').fetchall():
                result.append(RealUserDataToExcel(row[0], row[1], row[2], row[3]))
            return result

    def delete_all_data(self):
        with self.connection:
            self.cursor.execute('DELETE FROM feedbacks').fetchall()        
            self.cursor.execute('DELETE FROM answers').fetchall()
            self.cursor.execute('DELETE FROM users').fetchall()
            self.cursor.execute('DELETE FROM last_activities').fetchall()

    def close(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()