# nested_data = [1, [2, 3], [4, [5, 6]], 7]
# Напишите рекурсивную функцию recursive_sum(data: list) ->
# int, которая посчитает сумму всех чисел в такой «матрешке».
# (Ожидаемый результат для nested_data: 28)


nested_data = [1, [2, 3], [4, [5, 6]], 7]

def recursive_sum(data: list) -> int:
    total = 0
    for item in data:
        
        if isinstance(item, list):
            total += recursive_sum(item)
        
        elif isinstance(item, (int, float)):
            total += item
    
    return total

print(recursive_sum(nested_data))