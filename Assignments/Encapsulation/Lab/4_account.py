class Account:
    def __init__(self, id: int, balance, pin: int):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, new_pin):
        self.pin = new_pin

    def get_id(self, pin: int):
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin: int, new_pin: int):
        if old_pin == self.pin:
            self.pin = new_pin
            return "Pin changed"
        return "Wrong pin"


