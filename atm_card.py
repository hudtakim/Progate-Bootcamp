class ATMCard():
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def get_defaultPin(self):
        return self.defaultPin
    
    def get_defaultBalance(self):
        return self.defaultBalance