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
1. Credit Card
2. Debit Card
3. UPI
4. Net Banking"""
print(menu)

choice = input("Enter choice (1-4): ")
amount = float(input("Enter amount: "))
 
if choice == "1":
    strategy = CreditCard()
elif choice == "2":
    strategy = DebitCard()
elif choice == "3":
    strategy = UPI()
elif choice == "4":
    strategy = NetBanking()
else:
    strategy = None
 
if strategy is None:
    print("Invalid choice")
else:
    p = Payment_context(strategy)
    p.pay(amount)
