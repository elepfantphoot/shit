class Package:
    count_package_id = 0

    def __init__(self, Departure, Return, Duration, Destination, Airline, Adult_price, Child_price, Infant_price):
        Package.count_package_id += 1
        self.__package_id = Package.count_package_id
        self.__Departure = Departure
        self.__Return = Return
        self.__Duration = Duration
        self.__Destination = Destination
        self.__Airline = Airline
        self.__Adult_price = Adult_price
        self.__Child_price = Child_price
        self.__Infant_price = Infant_price

    def get_package_id(self):
        return self.__package_id

    def set_package_id(self, Package_id):
        self.__Package_id = Package_id

    def get_Departure(self):
        return self.__Departure

    def set_Departure(self, Departure):
        self.__Departure = Departure

    def get_Return(self):
        return self.__Return

    def set_Return(self, Return):
        self.__Return = Return

    def get_Duration(self):
        return self.__Duration

    def set_Duration(self, Duration):
        self.__Duration = Duration

    def get_Destination(self):
        return self.__Destination

    def set_Destination(self, Destination):
        self.__Destination = Destination

    def get_Airline(self):
        return self.__Airline

    def set_Airline(self, Airline):
        self.__Airline = Airline

    def get_Adult_price(self):
        return self.__Adult_price

    def set_Adult_price(self, Adult_price):
        self.__Adult_price = Adult_price

    def get_Child_price(self):
        return self.__Child_price

    def set_Child_price(self, Child_price):
        self.__Child_price = Child_price

    def get_Infant_price(self):
        return self.__Infant_price

    def set_Infant_price(self, Infant_price):
        self.__Infant_price = Infant_price

