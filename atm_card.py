from typing import DefaultDict


class ATMCard():
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def info(self):
        print("Default PIN:", self.defaultPin)
        print("Default Balance:", self.defaultBalance)

account1 = ATMCard(123, 5000)

