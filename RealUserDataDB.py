class RealUserDataDB:

    def __init__(self, user_id, initials, phone):
        self.user_id = user_id
        self.phone = phone
        self.initials = initials

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