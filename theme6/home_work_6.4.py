# Создайте функцию 
# business_card(name, surname, **kwargs) 
# Обязательные параметры: 
# ● имя; 
# ● фамилия. 
# Остальная информация передается через **kwargs.  
# Пример вызова 
# business_card( 
# "Иван", 
# "Иванов", 
# age=30, 
# city="Минск", 
# company="Google", 
# email="ivan@gmail.com" 
# ) 







def business_card(name, surname, **kwargs):
    full_name = f"{name} {surname}"
    
    border = "=" * 21
    print(border)
    print(full_name)
    
    for key, value in kwargs.items():
        label = key.capitalize()
        print(f"{label}: {value}")
    
    return None
business_card(
    "Иван",
    "Иванов",
    age=30,
    city="Минск",
    company="Google",
    email="ivan@gmail.com"
)