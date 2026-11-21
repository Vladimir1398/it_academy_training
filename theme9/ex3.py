# Дана строка
# text = "functional programming"
# Создайте словарь, где ключ — символ, значение — количество
# его появлений.
# Пробелы учитывать не нужно.


text = "functional programming"

counts = {ch: text.count(ch) for ch in set(text) if ch != " "}

print(counts)