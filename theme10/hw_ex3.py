# Напишите декоратор limit_calls, который ограничивает 
# количество вызовов функции. 
# Декоратор принимает три параметра: 
# ● limit — максимальное количество вызовов; 
# ● message — сообщение, которое выводится после 
# достижения лимита; 
# ● default — значение, которое возвращается вместо 
# результата функции после достижения лимита. 
# Пример: 
# @limit_calls( 
# limit=3, 
# message="Лимит вызовов исчерпан!", 
# default=None 
# ) 
# def get_data(name, age): 
# print(f"Получаем данные: {name}, {age}") 
# return f"{name}: {age}" 
# print(get_data("Иван", 20)) 
# print(get_data("Анна", 25)) 
# print(get_data("Петр", 30)) 
# print(get_data("Мария", 22)) 
# Первые три вызова должны выполнить функцию. 
# Четвёртый и последующие вызовы должны вывести: 
# Лимит вызовов исчерпан! 
# и вернуть: 
# None 
# При этом декоратор должен сохранять количество вызовов 
# отдельно для каждой декорированной функции. 
# Например: 
# @limit_calls(2, "Лимит!", 0) 
# def add(a, b): 
# return a + b 
# @limit_calls(3, "Больше нельзя!", []) 
# def get_items(category): 
# return ["item1", "item2"] 
# У add и get_items должны быть независимые счётчики. 
# Дополнительное условие: декорируемая функция может 
# принимать любое количество *args и **kwargs.






import functools

def limit_calls(limit, message, default):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if wrapper.calls >= limit:
                print(message)
                return default
            wrapper.calls += 1
            return func(*args, **kwargs)

        wrapper.calls = 0
        return wrapper
    return decorator

@limit_calls(limit=3, message="Лимит вызовов исчерпан!", default=None)
def get_data(name, age):
    print(f"Получаем данные: {name}, {age}")
    return f"{name}: {age}"

print(get_data("Иван", 20))
print(get_data("Анна", 25))
print(get_data("Петр", 30))
print(get_data("Мария", 22))


@limit_calls(2, "Лимит!", 0)
def add(a, b):
    return a + b

@limit_calls(3, "Больше нельзя!", [])
def get_items(category):
    return ["item1", "item2"]

print(add(1, 2))
print(add(1, 2))
print(add(1, 2))

print(get_items("a"))
print(get_items("a"))
print(get_items("a"))
print(get_items("a"))