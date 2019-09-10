class UsersFeedbackData:

    def __init__(self, user_id, initials, phone, feedback):
        self.user_id = user_id
        self.phone = phone
        self.initials = initials
        self.feedback = feedback

    def get_user_id(self):
        return self.user_id

    def get_phone(self):
        return self.phone

    def get_initials(self):
        return self.initials

    def get_feedback(self):
        return self.feedback