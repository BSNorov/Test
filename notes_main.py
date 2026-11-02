# number = 1
#
# while number <= 5:
#     print(number)
#     number += 1

# number = 1
#
# while number <= 5:
#     print(number)


# password = ""
#
# while password != "python123":
#     password = input("Введите пароль: ")
#
# print("Доступ разрешён! 🔓")


"""Угадай число"""

secret = 7
guess = 0

while guess != secret:
    guess = int(input("Угадай число от 1 до 10: "))

    if guess < secret:
        print("Загаданное число больше!")

    elif guess > secret:
        print("Загаданное число меньше!")

print("Поздравлю! Ты угадал!🎉")
