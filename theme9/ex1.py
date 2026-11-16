# Напишите рекурсивную функцию find_file(folder, 
# target_filename), которая ищет полный путь к 
# целевому файлу в словаре-дереве и возвращает строку с 
# путем или None. 



def find_file(folder, target_filename):
    for name, value in folder.items():
        if name == target_filename:
            return name
        if isinstance(value, dict):
            result = find_file(value, target_filename)
            if result is not None:
                return name + "/" + result
    return None


file_system = { 
    "documents": { 
        "work": { 
            "project_notes.txt": "content", 
            "budget.xlsx": "content" 
        }, 
        "personal": { 
            "passport.pdf": "content" 
        } 
    }, 
    "photos": { 
        "vacation.jpg": "content" 
    } 
}

print(find_file(file_system, "budget.xlsx"))     # documents/work/budget.xlsx
print(find_file(file_system, "vacation.jpg"))    # photos/vacation.jpg
print(find_file(file_system, "resume.docx"))     # None