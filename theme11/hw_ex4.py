# 1. Прочитать файл matches.json. 
# 2. Посчитать общий K/D (отношение убийств к смертям) 
# для каждого игрока по всем матчам, округлив до 2 знаков 
# после запятой. 
# 3. Найти лучшего игрока (с самым высоким K/D). 
# 4. Сохранить результат в файл leaderboard.json, 
# отсортировав игроков от лучшего к худшему. 


import json

with open("matches.json", "r", encoding="utf-8") as f:
    matches = json.load(f)

stats = {}
for match in matches:
    for player in match["players"]:
        nick = player["nickname"]
        if nick not in stats:
            stats[nick] = [0, 0]
        stats[nick][0] += player["kills"]
        stats[nick][1] += player["deaths"]

leaderboard = []
for nick, (kills, deaths) in stats.items():
    kd = round(kills / deaths, 2) if deaths > 0 else float("inf")
    leaderboard.append({
        "nickname": nick,
        "kills": kills,
        "deaths": deaths,
        "kd": kd
    })


leaderboard.sort(key=lambda p: p["kd"], reverse=True)

with open("leaderboard.json", "w", encoding="utf-8") as f:
    json.dump(leaderboard, f, ensure_ascii=False, indent=4)


print("Таблица лидеров:")
for place, player in enumerate(leaderboard, start=1):
    best = " <- лучший игрок" if place == 1 else ""
    print(f"{place}. {player['nickname']}: K/D = {player['kd']} "
          f"({player['kills']} убийств / {player['deaths']} смертей){best}")