class key_info:
    count_key_info_id = 0  # A class attribute

    def __init__(self, adult, child, infant):
        key_info.count_key_info_id += 1
        self.__key_info_id = key_info.count_key_info_id # private attribute
        self.__adult = adult
        self.__child = child
        self.__infant = infant

    def get_key_info_id(self):
        return self.__key_info_id

    def set_key_info_id(self, id):
        self.__key_info_id = id

    def get_adult(self):
        return self.__adult

    def set_adult(self, adult):
        self.__adult = adult

    def get_child(self):
        return self.__child

    def set_child(self, child):
        self.__child = child

    def get_infant(self):
        return self.__infant

    def set_infant(self, infant):
        self.__infant = infant

