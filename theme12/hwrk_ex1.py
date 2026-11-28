# Создайте класс Car, описывающий автомобиль.Реализуйте 
# приватные атрибуты для марки (__make), модели (__model) и 
# пробега (__mileage). 
# Добавьте геттер и сеттер для пробега.  
# В сеттере проверьте условие: пробег не может быть 
# отрицательным числом, а также не может уменьшаться 
# (новый пробег должен быть больше или равен старому). 



class Car:
    def __init__(self, make: str, model: str, mileage: int = 0):
        self.__make = make
        self.__model = model
        self.__mileage = 0
        self.mileage = mileage


    @property
    def mileage(self) -> int:
        return self.__mileage

    @mileage.setter
    def mileage(self, value: int) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Пробег должен быть числом")
        if value < 0:
            raise ValueError("Пробег не может быть отрицательным")
        if value < self.__mileage:
            raise ValueError(f"Пробег не может уменьшаться: текущий {self.__mileage}, \n"f"новый {value}")
        self.__mileage = value
        
        
    def __str__(self) -> str:
        return f"Car: {self.__make}\nModel: {self.__model}\nMileage: {self.__mileage} км\n"



# if __name__ == "__main__":
#     car = Car("Toyota", "Camry", 15000)
#     print(car)
    
# car.mileage = 16000
# print(car.mileage)