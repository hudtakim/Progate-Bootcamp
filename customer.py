import atm_card

class Customer():
    def __init__(self, id, custPin=1234, custBalance=10000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def get_id(self):
        return self.id
    
    def get_custPin(self):
        return self.custPin

    def get_custBalance(self):
        return self.custBalance

    def withdrawBalance(self, nominal):
        self.custBalance -= nominal

    def depositBalance(self, nominal):
        self.custBalance += nominal
