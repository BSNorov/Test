"""Кортеж - упорядоченная коллекция, эелменты которой нельзя изменять после создания"""

# coordinates = (120, 64, 300)
#
# print(coordinates)
# print(coordinates[0])
# print(coordinates[-1])

# a = (5,)
# print(type(a))


"Словарь - коллекция, которая хранит пары 'ключ - значение'"

player = {
    "name": 'Steve',
    "health": 100,
    "level": 5,
    "coins": 250
}

# print(player)
# print(player['name'])
# print(player['health'])

# player['health'] = 70                       # изменяем значение
# print(player['health'])

# player['weapon'] = "Алмазный меч"           # добаялем новые данные
# print(player)
#
# player.pop('weapon')
# print(player)


print(player.get('name'))
print(player.get('pet'))
