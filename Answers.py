class Answers:

    def __init__(self, question_id, answer_text):
        self.question_id = question_id
        self.answer_text = answer_text

    def get_question_id(self):
        return self.question_id

    def get_answer_text(self):
        return self.answer_text