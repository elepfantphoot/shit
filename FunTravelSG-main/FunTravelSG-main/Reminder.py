class Reminder:
    count_id = 0  # A class attribute

    def __init__(self, name, reminder_type, information):
        Reminder.count_id += 1
        self.__reminder_id = Reminder.count_id  # private attribute
        self.__name = name
        self.__reminder_type = reminder_type
        self.__information = information

    def get_reminder_id(self):
        return self.__reminder_id

    def get_name(self):
        return self.__name

    def get_reminder_type(self):
        return self.__reminder_type

    def get_information(self):
        return self.__information

    def set_reminder_id(self, reminder_id):
        self.__reminder_id = reminder_id

    def set_name(self, name):
        self.__name = name

    def set_reminder_type(self, reminder_type):
        self.__reminder_type = reminder_type

    def set_information(self, information):
        self.__information = information
