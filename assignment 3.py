class CreditCard:
    def pay(self, amount):
        print(f"Payment of Rs{amount} made using Credit Card")

class DebitCard:
    def pay(self, amount):
        print(f"Payment of Rs{amount} made using Debit Card")

class UPI:
    def pay(self, amount):
        print(f"Payment of Rs{amount} made using UPI")

class NetBanking:
    def pay(self, amount):
        print(f"Payment of Rs{amount} made using Net Banking")

class Payment_context:
    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)

menu = """Select Payment Method

