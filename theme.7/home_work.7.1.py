# Напишите функцию is_palindrome(text), которая: 
# ● принимает строку; 
# ● игнорирует регистр букв и пробелы; 
# ● возвращает True, если строка является палиндромом, 
# иначе False. 


def is_palindrome(text: str) -> bool:
    
    cleaned = text.lower().replace(" ", "")
   
    return cleaned == cleaned[::-1]

print(is_palindrome("Привет"))                    
print(is_palindrome("Шалаш"))