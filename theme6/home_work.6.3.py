# Напишите функцию 
# analyze_grades(*grades) 
# которая возвращает словарь 
# { 
# } 
# "count": ., 
# "average": ., 
# "highest": ., 
# "lowest": ., 
# "passed": . 
# где 
# ● passed — количество оценок больше либо равно 60. 
# Если оценки отсутствуют — вернуть None.




def analyze_grades(*grades):
    # Если оценок нет — возвращаем None
    if not grades:
        return None

    count = len(grades)
    average = sum(grades) / count
    highest = max(grades)
    lowest = min(grades)
    passed = sum(1 for grade in grades if grade >= 60)

    return {
        "count": count,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passed": passed
    }
result = analyze_grades(55, 70, 88, 60, 45)
print(result)