# print('Игрок подпрыгнул!')
# print("Игрок приземлился!")
#
# print('Игрок подпрыгнул!')
# print("Игрок приземлился!")
#
# print('Игрок подпрыгнул!')
# print("Игрок приземлился!")

# def jump():
#     print('Игрок подпрыгнул!')
#     print("Ирок приземлился!")
#
# jump()
# jump()
# jump()



# def hello():
#     print("Я внутри функции!")
#
# print("Начало программы")
# hello()
# print("Конец программы")


'''Имена функции'''

# Правильно
# def show_score():
#     print(100)
#
# def player_attack():
#     print("Атака!")
#
# def hello2():
#     print("Привет")


# Неправильно

# def 2hello():
#     pass
#
# def my function():
#     pass

'''Параметры'''

# def hello_alex():
#     print("Привет, Алекс!")
#
# def hello_masha():
#     print("Привет, Маша!")
#
# def hello_dima():
#     print("Привет, Дима!")
#
# hello_alex()
# hello_masha()
# hello_dima()

# def hello(name):
#     print("Привет,", name)
#
# hello("Алекс")
# hello("Маша")
# hello("Дима")
#


# def create_hero(name, level, hp):
#     print("Герой:", name)
#     print("Уровень:", level)
#     print("Здоровье:", hp)
#
# create_hero("Ниндзя", 5, 100)


# def create_hero(name, level, hp):
#     print("Герой:", name)
#     print("Уровень:", level)
#     print("Здоровье:", hp)
#
# name = input("Введите имя вашего героя: ")
# level = int(input("Уровень вашего героя: "))
# hp = int(input("Здоровье вашего героя: "))
# create_hero(name, level, hp)


# def add(a, b):
#     print(a + b)
# 
# result = add(5, 3)
# print("Результат:", result)

def add(a, b):
    return a + b

result = add(5, 3)
print("Результат:", result)
