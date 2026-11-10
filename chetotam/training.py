# Напишите декоратор retry(func).

# Внутри создайте функцию-обертку wrapper(*args, **kwargs).

# Обертка должна пытаться выполнить целевую функцию func.

# Если функция выполнилась успешно — вернуть её результат.

# Если при выполнении возникла ошибка Exception, перехватить её (try-except), вывести в консоль сообщение:
#  «Произошла ошибка [название ошибки]. Пробуем еще раз...» и сделать вторую (повторную) попытку вызова.

# Не забудьте обернуть wrapper с помощью @functools.wraps(func).

import functools

def retry(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        try:
            return func(*args, **kwargs)
        except Exception as err:
            error_name = type(err).__name__
            print(f"Произошла ошибка!{error_name}. Попробуем ещё раз")
            try:
                return func(*args, **kwargs)
            except Exception as second_e:
                raise second_e
    return wrapper

@retry
def risky_operation(x):
    if x < 0:
        raise ValueError("Отрицательное значение!")
    return x * 2

print(risky_operation(5))