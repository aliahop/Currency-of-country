class Switzerland():
    def __init__(self, currency) :
        self.currency = currency
    def display(self):
        return "Currency: " + self.currency
class England():
    def __init__(self, currency) :
        self.currency = currency
    def display(self):
        return "Currency: " + self.currency
class Japan():
    def __init__(self, currency) :
        self.currency = currency
    def display(self):
        return "Currency: " + self.currency

new_currency = Switzerland('franc')
new_currency1 = England('pound')
new_currency2 = Japan('yen')
