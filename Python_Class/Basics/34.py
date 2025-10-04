class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self._name} deposited ₹{amount}")
        else:
            print("Invalid deposit amount")


    def check_balance(self):
        print(f"{self._name}'s balance: ₹{self.__balance}")


account1 = BankAccount("Ravi", 5000)
account1.deposit(2000)
account1.check_balance()
# print(account1.__balance)

