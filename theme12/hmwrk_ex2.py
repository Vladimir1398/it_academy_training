# Создайте класс BankAccount, который представляет 
# банковский счёт. У объекта должны быть: 
# owner — имя владельца; _balance — текущий баланс. 
# Реализуйте методы: 
# ● deposit(amount) — пополнение счёта; 
# ● withdraw(amount) — снятие денег; 
# ● get_balance() — получение текущего баланса. 
# Правила: 
# ● нельзя пополнить счёт на отрицательную или нулевую 
# сумму; 
# ● нельзя снять отрицательную или нулевую сумму; 
# ● нельзя снять больше денег, чем есть на счёте



class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount: float) -> None:

        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля")
        if amount > self._balance:
            raise ValueError(f"Недостаточно средств: баланс {self._balance}\n"f"Запрошено {amount}")
        self._balance -= amount
    
    
    def get_balance(self) -> float:
        return self._balance

    def __str__(self) -> str:
        return f"Счёт владельца {self.owner}: {self._balance} руб."


