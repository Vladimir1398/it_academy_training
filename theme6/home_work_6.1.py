# Дан список идентификаторов пользователей.   
# Найдите первый элемент, который встретился повторно. 
# Результат: 
# Первый повтор: 42 
# Если повторов нет: 
# Повторов нет 
# Ограничения 
# ● Нельзя использовать list.count(). 
# ● Нельзя использовать вложенные циклы. 




users = [15, 42, 18, 90, 11, 42, 35, 18] 

one_repeat = set()
first_dublicate = None

for users_id in users:
    if users_id in one_repeat:
        first_dublicate = users_id
        break
    one_repeat.add(users_id)
if first_dublicate is not None:
    print(f"Первый повтор: {first_dublicate}")
else:
    print(f"Повторов нет")