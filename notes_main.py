# age = 18            # int
# name = "Alex"       # str
# price = 19.5        # float

'''bool - Логический тип данных (Булевый)
True - истина (да)
False - ложь (нет)
'''

# player_alive = True
# has_weapon = False
#
# print(player_alive)
# print(has_weapon)
# print(type(player_alive))


# age = 16
# print(age >= 18)
# print(10 > 5)

"""
Операторы сравнения:
1) == - Равно
2) != - НЕ равно
3) > - Больше
4) < - Меньше
5) >= - Больше или Равно
6) <= - Меньше или Равно
"""

# money = 650
# phone_price = 800
#
# print(money >= phone_price)


# password = "hello123"
# print(password == "python123")

"""Условный оператор
if - если

Конструкция:
if условие:
    действие
"""

# age = 16
#
# if age >= 18:
#     print("Добро пожаловать в игру!")

# secret_code = 777
#
# code = int(input("Введите секретный код: "))
#
#
# if code == secret_code:
#     print("🔓Секретная дверь открыта!")

"""else - иначе

Конструкция:

if условие:
    действие_1
else:
    действие_2
"""

# password = input("Введите пароль: ")
# if password == "python123":
#     print("✅Доступ разрешён!")
# else:
#     print("❌Неверный пароль!")


# print(10 % 2)
# print(7 % 2)

# number = int(input("Введите число: "))
# if number % 2 == 0:
#     print("Число чётное")
# else:
#     print("Число нечётное")

"""elif (else + if) - иначе, если"""


score = int(input("Введите количество баллов: "))

if score >= 90:
    print("🏆 Легенда!")
elif score >= 70:
    print("🥇Профессионал!")
elif score >= 50:
    print("🥈Новичок")
else:
    print("💪Нужно больше тренироваться!")
