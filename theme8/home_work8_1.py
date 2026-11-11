# Дан список попыток входа: 
# logs = [ 
# ("alice", True), 
# ("bob", False), 
# ("alice", True), 
# ("alice", False), 
# ("bob", True), 
# ("charlie", False), 
# ] 
# Напишите функцию 
# analyze_logins(logs) 
# которая возвращает словарь вида 
# { 
# } 
# "alice": {"success": 2, "failed": 1}, 
# "bob": {"success": 1, "failed": 1}, 
# "charlie": {"success": 0, "failed": 1},



def analyze_logins(logs):
    result = {}
    
    for name, success in logs:
        if name not in result:
            result[name] = {"success": 0, "failed": 0}
        if success:
            result[name]["success"] += 1
        else:
            result[name]["failed"] += 1
    
    return result


logs = [
    ("alice", True),
    ("bob", False),
    ("alice", True),
    ("alice", False),
    ("bob", True),
    ("charlie", False),
]

print(analyze_logins(logs))