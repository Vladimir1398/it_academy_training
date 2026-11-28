class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть > 0")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть > 0")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount

    def _change_balance(self, delta):
        if self.__balance + delta < 0:
            raise ValueError("Баланс не может стать отрицательным")
        self.__balance += delta


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self._interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self._interest_rate
        self.deposit(interest)
        return interest


class CreditAccount(BankAccount):
    def __init__(self, owner, balance=0, credit_limit=1000):
        super().__init__(owner, balance)
        self.__credit_limit = credit_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть > 0")
        if self.balance - amount < -self.__credit_limit:
            raise ValueError("Превышен кредитный лимит")
        self._change_balance(-amount)


base = BankAccount("Иван", 1000)
base.deposit(500)
base.withdraw(200)
print(base.balance)

sav = SavingsAccount("Мария", 10_000, 0.05)
sav.apply_interest()
print(sav.balance)

cred = CreditAccount("Пётр", 500, 2000)
cred.withdraw(1500)
print(cred.balance)