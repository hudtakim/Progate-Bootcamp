from atm_card import ATMCard

class Customer():
    def __init__(self, id, custPin=1234, custBalance=10000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    @property
    def get_id(self):
        return self.id
    
    @property
    def get_custPin(self):
        return self.custPin
    
    @property
    def get_custBalance(self):
        return self.custBalance

    def withdrawBalance(self, nominal):
        self.custBalance -= nominal

    def depositBalance(self, nominal):
        self.custBalance += nominal
