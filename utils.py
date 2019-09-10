import string_worker
import config, time
from operator import itemgetter, attrgetter
import xlsxwriter
import Questions

def generate_list_users(db_worker):
    workbook = xlsxwriter.Workbook(config.users_file)
    users = db_worker.select_all_real_users_to_excel()
    finished_users = []
    unfinished_users = []
    nonstarted_users = []
    for user in users:
        user.set_answers(db_worker.select_all_answers_by_user(user.get_user_id()))
        if user.get_count_answers() == 0:
            nonstarted_users.append(user)
        elif user.get_count_answers() == Questions.get_questions_limit():
            finished_users.append(user)
        else:
            unfinished_users.append(user)
    fill_worksheet_by_users(workbook.add_worksheet('Закончили') , finished_users, workbook.add_format({'bold': True}))
    fill_worksheet_by_users(workbook.add_worksheet('Не закончили') , unfinished_users, workbook.add_format({'bold': True}))
    fill_worksheet_by_users_without_questions(workbook.add_worksheet('Не начали') , nonstarted_users, workbook.add_format({'bold': True}))
    fill_worksheet_by_users_without_questions(workbook.add_worksheet('Не вошли в бот') , db_worker.select_all_users_not_in_bot(), workbook.add_format({'bold': True}))
    fill_worksheet_by_users_without_questions(workbook.add_worksheet('Не в Telegram') , db_worker.select_all_users_not_exist(), workbook.add_format({'bold': True}))
    fill_worksheet_by_users_feedbacks(workbook.add_worksheet('Фидбек'), db_worker.select_all_users_feedbacks(), workbook.add_format({'bold': True}))
    workbook.close()


def fill_worksheet_by_users(worksheet, users, bold):
    worksheet.write(0, 0, "Имя и Фамилия", bold)
    worksheet.write(0, 1, "Телефон", bold)
    worksheet.set_column(0, 1 + Questions.get_count_questions(), 15)
    for j in range(Questions.get_count_questions()):
        worksheet.write(0, 2 + j, "Вопрос {}".format(j + 1), bold)
    users.sort(key=lambda x: (x.get_last_activity()))
    i = 1
    for user in users:
        worksheet.write(i, 0, user.get_initials())
        worksheet.write(i, 1, user.get_phone())
        for answer in user.get_answers():
            worksheet.write(i, 2 + answer.get_question_id(), answer.get_answer_text())
        i += 1
    return worksheet

def fill_worksheet_by_users_without_questions(worksheet, users, bold):
    worksheet.write(0, 0, "Имя и Фамилия", bold)
    worksheet.write(0, 1, "Телефон", bold)
    worksheet.set_column(0, 1, 15)
    i = 1
    for user in users:
        worksheet.write(i, 0, user.get_initials())
        worksheet.write(i, 1, user.get_phone())
        i += 1
    return worksheet

def fill_worksheet_by_users_feedbacks(worksheet, users, bold):
    worksheet.write(0, 0, "Имя и Фамилия", bold)
    worksheet.write(0, 1, "Телефон", bold)
    worksheet.write(0, 2, "Фидбек", bold)
    worksheet.set_column(0, 2, 15)
    i = 1
    total_feedback = 0
    for user in users:
        worksheet.write(i, 0, user.get_initials())
        worksheet.write(i, 1, user.get_phone())
        worksheet.write(i, 2, int(user.get_feedback()))
        i += 1
        total_feedback = int(user.get_feedback())
    worksheet.write(0, 6, 'Total', bold)
    # print(i)
    worksheet.write(0, 7, '{}/{}'.format(total_feedback, i - 1))
    return worksheet