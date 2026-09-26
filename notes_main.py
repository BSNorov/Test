# number = 1
#
# while number <= 5:
#     print(number)
#     number += 1


# for i in range(1, 6):
#     print(i)
#
# number = 1
#
# while number <= 5:
#     print(number)
#     number += 1


# password = ""
#
# while password != "python123":
#     password = input("Введите пароль: ")
#
# print("Доступ разрешён!")


# battery = 10
#
# while battery < 100:
#     battery += 10
#     print("Заряд:", battery, "%")
#
# print('Телефон полностью заряжен!')


money = 200

while money >= 50:
    print("У тебя осталось:", money)

    answer = input("Купить шоколадку за 50 рублей? да/нет: ")

    if answer == "да":
        money -= 50
        print("Шоколад куплена!")
    else:
        print("Покупки завершены!")
        break

print("Осталось денег:", money)
