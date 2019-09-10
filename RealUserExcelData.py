class RealUserExcelData:

    def __init__(self, initials, phone):
        self.phone = phone
        self.initials = initials

    def get_phone(self):
        return self.phone 

    def get_initials(self):
        return self.initials

    def get_first_name(self):
        return self.initials.split()[0]

    def get_last_name(self):
        return self.initials.split()[1]
