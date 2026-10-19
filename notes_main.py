"""Кортеж"""

# base = ([45, 90])
# print(base)
# print(base[0])
# print(base[1])
# print(type(base))

# base[0] = 100
# print(base)       # Ошибка

# hero = ("Ниндзя", 15, 'Катана')
# print(hero[0])
# print(hero[1])

# b = (5,)
# print(type(b))



"""Словарь"""

player = {
    'name': 'Стив',
    'health': 20,
    'level': 5,
    'weapon': 'Меч'
}

# print(player['name'])
# print(player['health'])
# player['health'] = 10       # Изменение внесли
# print(player['health'])

# player['pet'] = 'Волк'      # Добавили ключ
# print(player)

# print(player['strength'])
print(player.get('strength'))
