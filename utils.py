class Item:
    pay_rate = 1
    all = []

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.all += (self, name, price, count)

    def returned(self):
        desc = str(self.name) + " " + self.price + self.count
        return desc.title()

    def calculate_total_price(self):
        self.total_price = self.price * self.count * self.pay_rate
        return self.total_price
    def apply_discount(self):
        self.price = self.price * self.pay_rate
