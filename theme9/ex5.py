# Дан список 
# files = [ 
# "main.py", 
# "test.py", 
# "README.md", 
# "data.csv", 
# "notes.txt" 
# ] 
# Оставьте только Python-файлы. 
# Используйте filter.


files = ["main.py", "test.py", "README.md", "data.csv", "notes.txt"]

py_files = list(filter(lambda f: f.endswith(".py"), files))

print(py_files)