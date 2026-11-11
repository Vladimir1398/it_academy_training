# Создайте функцию: 
# convert(value, from_unit, to_unit) 
# Поддерживаемые единицы: 
# km 
# m 
# cm 
# Примеры: 
# convert(5, "km", "m") 
# Результат: 
# 5000 
# convert(350, "cm", "m")



def convert(value, from_unit, to_unit):
        
    units = {
    "km": 1000,   
    "m": 1,       
    "cm": 0.01  
    }
    
    if from_unit not in units or to_unit not in units:
        return None

    in_meters = value * units[from_unit]
    result = in_meters / units[to_unit]

    return result


print(convert(5, "km", "m"))      
print(convert(350, "cm", "m"))
