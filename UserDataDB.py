class UserDataDB:

    def __init__(self, Id, first_name, last_name, user_name, last_activity):
        self.id = Id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.last_activity = last_activity

    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_user_name(self):
        return self.user_name

    def get_last_activity(self):
        return self.last_activity

    def set_answers(self, answers):
        self.answers = answers

    def get_answers(self):
        return self.answers

    def get_count_answers(self):
        return len(self.answers)