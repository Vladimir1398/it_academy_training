# Напиши программу, которая выводит простую таблицу 
# умножения для чисел от 1 до 5. 
# Результат должен быть аккуратно выведен в виде сетки 
# (квадрата), где на пересечении строки и столбца стоит 
# результат их умножения. 
# Пример: 
# 1  2  3  4  5   
# 2  4  6  8  10   
# 3  6  9  12 15   
# 4  8  12 16 20   
# 5  10 15 20 25 



size = 5

max_value = size * size
cell_width = len(str(max_value)) + 1  

for i in range(1, size + 1):
    row = []
    for j in range(1, size + 1):
        product = i * j
        row.append(f"{product:>{cell_width}}")
    print("".join(row))

