class RealUserDataToExcel:

    def __init__(self, user_id, initials, phone, last_activity):
        self.user_id = user_id
        self.phone = phone
        self.initials = initials
        self.last_activity = last_activity

    def get_user_id(self):
        return self.user_id

    def get_phone(self):
        return self.phone

    def get_initials(self):
        return self.initials

    def get_first_name(self):
        return self.initials.split()[0]

    def get_last_name(self):
        return self.initials.split()[1]

    def get_last_activity(self):
        return self.last_activity

    def set_answers(self, answers):
        self.answers = answers

    def get_answers(self):
        return self.answers

    def get_count_answers(self):
        return len(self.answers)