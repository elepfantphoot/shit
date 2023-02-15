class transactions:
    count_transaction_id = 0

    def __init__(self, card_name, card_number, expiry, cvc, default_card, remember_card):
        transactions.count_transaction_id += 1
        self.__transaction_id = transactions.count_transaction_id
        self.__card_name = card_name
        self.__card_number = card_number
        self.__expiry = expiry
        self.__cvc = cvc
        self.__default_card = default_card
        self.__remember_card = remember_card

    def get_transaction_id(self):
        return self.__transaction_id

    def set_user_id(self, transaction_id):
        self.__transaction_id = transaction_id

    def get_card_name(self):
        return self.__card_name

    def set_card_name(self, card_name):
        self.__card_name = card_name

    def get_expiry(self):
        return self.__expiry

    def set_expiry(self, expiry):
        self.__expiry = expiry

    def get_cvc(self):
        return self.__cvc

    def set_cvc(self, cvc):
        self.__cvc = cvc

    def get_default_card(self):
        return self.__default_card

    def set_default_card(self, default_card):
        self.__default_card = default_card

    def get_remember_card(self):
        return self.__remember_card

    def set_remember(self, remember_card):
        self.__remember_card = remember_card

