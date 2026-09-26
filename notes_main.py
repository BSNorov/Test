"""
for - используется, когда мы перебираем элементы или выполняем действия
определённое количество раз


while - выполняет действия, пока определённое условие остаётся истинным
"""

# for i in range(5):
#     print("Привет, человек!")

# for i in range(5):
#     print(i)

# for i in range(3):
#     print("Python")


'''
Вариант 1
'''
# for i in range(5):
#     print(i)

'''
Вариант 2
'''
# for i in range(1, 6):
#     print(i)

'''
Вариант 3
'''
# for i in range(2, 11, 2):
#     print(i)


# for i in range(10, 0, -1):
#     print(i)


# print("Подготовка к запуска!")
#
# for i in range(10, 0, -1):
#     print(i)
#
# print('🚀 РАКЕТА ЗАПУЩЕНА!')

# heroes = ['Бэтмен', 'Железный человек', 'Тор', 'Халк']
#
# for hero in heroes:
#     print("Добро пожаловать,", hero)


# fruits = ['Яблоко', 'Банан', 'Апельсин']
#
# for fruit in fruits:
#     print(fruit)


# age = "Саша"
# print(age)

coins = 0

for i in range(5):
    coins = coins + 10
    print("Монеты:", coins)

print("Всего заработано:", coins)
