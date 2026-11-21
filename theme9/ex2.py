# words = [ 
#     "Python", 
#     "java", 
#     "C++", 
#     "Rust", 
#     "Go", 
# "Swift", 
# "PHP" 
# ] 
# Получите новый список, содержащий слова длиной не менее 
# пяти символов в нижнем регистре.


words = ["Python", "java", "C++", "Rust", "Go", "Swift", "PHP"]

result = [w.lower() for w in words if len(w) >= 5]

print(result)