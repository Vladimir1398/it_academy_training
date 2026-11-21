# Создайте декоратор ignore_duplicates, который не позволяет 
# выполнить функцию два раза подряд с одинаковыми 
# аргументами. 
# Пример: 
# @ignore_duplicates 
# def send_message(text): 
# print(f"Отправлено: {text}") 
# Вызовы 
# send_message("Привет") 
# send_message("Привет") 
# send_message("Как дела?") 
# send_message("Как дела?") 
# send_message("Привет") 
# должны вывести 
# Отправлено: Привет 
# Повторный вызов проигнорирован. 
# Отправлено: Как дела? 
# Повторный вызов проигнорирован. 
# Отправлено: Привет 



import functools

def ignore_duplicates(func):
    last_args = []

    @functools.wraps(func)
    def wrapper(*args):
        if list(args) == last_args:
            print("Повторный вызов проигнорирован.")
            return None
        last_args[:] = list(args)
        return func(*args)
    return wrapper

@ignore_duplicates
def send_message(text):
    print(f"Отправлено: {text}")

send_message("Привет") 
send_message("Привет") 
send_message("Как дела?") 
send_message("Как дела?") 
send_message("Привет") 