# Напишите функцию longest_word(text), которая: 
# ● принимает строку; 
# ● находит самое длинное слово; 
# ● возвращает его. 
# Если слов одинаковой длины несколько — вернуть первое.



def longest_word(text: str) -> str | None:
    words = text.split()
    
    if not words:
        return None
    return max(words, key=len)

print(longest_word("кот собака котяра"))
print(longest_word("один два три"))             