import random
import emoji

limit = 15

questions = [
				emoji.emojize("Как часто нужно читать Уголовный и Уголовно-процессуальный кодексы Украины, чтобы быть успешным адвокатом уголовной практики?\n\n:speech_balloon: <i>С этим вопросом тебе поможет именно такой адвокат!</i> :winking_face: "), 
				emoji.emojize("Когда (число, месяц, год) было создано Адвокатское объединение Jurimex, с которого фактически начала активно развиваться уголовная практика? 🤔\n\n:speech_balloon:<i>Даем подсказку - сегодня с нами управляющий партнер Адвокатского объединения</i> 🙌"), 
				emoji.emojize("Что делать, если 1 января под ёлкой не оказалось подарка от Деда Мороза?😢 \n\n:speech_balloon:<i>Ответ знает адвокат, который расследовал дело про ноутбуки</i> 🔍"), 
				emoji.emojize("Как вычислить, какая рекламная кампания более эффективная?💡 \n\n:speech_balloon:<i>Ищи того,  кто создает ее!</i> 🎯"), 
				emoji.emojize("Как называется телеграмм-канал Taxlink?📲 \n\n:speech_balloon:<i>Познакомься с нашим CMM- менеджером)</i> ☝️"), 
				emoji.emojize("В каком году был сформирован отдел продаж?:money_with_wings: \n\n:speech_balloon:<i>Ответ знает РОП</i> 🤫"), 
				emoji.emojize("Какой предмет является символом власти в отделе продаж?:crown: \n\n:speech_balloon:<i>Любой специалист по продажам в Jurimex знает, что это …</i> ☝️"), 
				emoji.emojize("Каким инструментом чаще всего пользуется специалист отдела продаж в своей работе?\n\n:speech_balloon:<i>Скорее всего, того, кто вам нужен, стоит поискать возле бассейна</i>🏊 😜"), 
				emoji.emojize("Какой юрист может дать ответ на вопрос “Как мне законно платить меньше налогов?” \n\n:speech_balloon:<i>Подсказка, к кому обратиться, в самом вопросе</i>☝️"), 
				emoji.emojize("Какой основной продукт разрабатывает TAXACADEMY? :books: \n\n:speech_balloon: <i>Среди нас есть лекторы  TAXACADEMY</i>  :winking_face:"), 
				emoji.emojize('Сколько тендеров выиграли специалисты практики Международных отношений и инвестиций в 2018 году?\n\n:speech_balloon:<i>Поздравь коллегу с международного отдела с получением адвокатского свидетельства!</i>📄'), 
				emoji.emojize('Какой самый трудный период работы наших бухгалтеров?🔢'), 
				emoji.emojize("Какое количество товарных знаков подано на регистрацию в 2019?:copyright: \n\n:speech_balloon:<i>Интеллектуальная собственность с Jurimex под надежной защитой!</i>  🙌"), 
				emoji.emojize("Сколько кинопроектов при юридической поддержке Юримекс вышли в прокат в 2019?:movie_camera:  \n\n:speech_balloon:<i>Ни для кого ни секрет, кто Медийный Страж в компании Jurimex</i>😊 "), 
				emoji.emojize("Какой рост штата Jurimex наблюдается в 2019 году?  ⭐\n\n:speech_balloon:<i>Спроси у тех, кто принимал тебя на работу</i>:woman::briefcase:"), 
				emoji.emojize("С какой цифры начинается отсчет в сфере IT?➡️ \n\n:speech_balloon:<i>Спроси у тех, кто с компьютерами на “ты”</i> 💻"), 
				emoji.emojize("Что, на сленге айтишников, значит слово “кресты”?:heavy_plus_sign: "), 
				emoji.emojize("Для наших талантливых программистов любой баг это...  \n\n:speech_balloon:<i>Спроси у специалиста в сфере компьютерной науки</i>🤖"), 
				emoji.emojize("Какой отдел чаще всего заказывает переговорку для встреч? \n\n:speech_balloon:<i>Даём подсказку - ищи коллегу, которая получает твои письма</i> :love_letter:"), 
				emoji.emojize("Сколько пачек кофе расходится среди сотрудников Jurimex в месяц?☕ \n\n:speech_balloon:<i>Узнай у самой энергичной коллеги</i> 😂👯"), 
				emoji.emojize("Cотрудники какого этажа быстрее всех приходят за новой пачкой сахара?\n\n:speech_balloon:<i>Найди коллегу, у которой все вкусняшки офиса</i>:candy:"), 
				emoji.emojize("Каким не совсем юридическим навыком должен обладать хороший юрист в области копирайта?:black_nib: \n\n:speech_balloon:<i>Узнай, как дела у коллег с отдела интеллектуального права!</i> "), 
				emoji.emojize("Какое непрофильное образование имеют два специалиста отдела интеллектуальной собственности?:eyes: \n\n:speech_balloon:<i>Вы точно догадались, где их искать</i>:winking_face:  "), 
				emoji.emojize("Дата и месяц Международного дня интеллектуальной  собственности🔏 \n\n:speech_balloon:<i>Узнай у тех, кто точно отмечает этот день!</i> "), 
				emoji.emojize("Какое количество консультаций предоставили юристы для проекта Bitlex.ua за время его существования?🔄 \n\n:speech_balloon:<i>Можно подсмотреть в дипломе руководителя проекта</i>😊"), 
				emoji.emojize("Сколько человек трудится в отделе налогового права?:busts_in_silhouette: 🤔"), 
				emoji.emojize("Какой доминирующий цвет платформы Taxlink?\n\n:speech_balloon:<i>Это цвет диплома руководителя практики налогового права</i>👍"),
				emoji.emojize("Какой слоган платформы Taxlink?:large_orange_diamond: \n\n:speech_balloon:<i>Подумай, кто мог его придумать?</i> 🤔"),
				emoji.emojize("Существует ли Международный день переводчика? Укажите дату\n\n:speech_balloon:<i>Возможно, кто-то в Jurimex празднует его?</i>🤫")
			]

def get_next_random_question_id(answers_id):
	candidates = []
	for possible_candidate in range(len(questions)):
		if not possible_candidate in answers_id:
			candidates.append(possible_candidate)
	return candidates[random.randint(0, len(candidates) - 1)]

def get_question(question_id):
	return questions[question_id]

def get_count_questions():
	return len(questions)

def get_questions_limit():
	return limit

def is_gif_time(time):
	return time == 1

def is_time_to_praise(time):
	return time == 6 or time == 11 or time == 2 or time == 3 or time == 14
# print(get_next_random_quesiton_id({2}))
