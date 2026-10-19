# a = "яблоко"
# b = "банан"
# c = "шоколадка"

'''Коллекция - это способ хранить несколько значений в одной переменной'''

"""Список"""

# items = ["меч", "кирка", "яблоко"]
# print(items)

# print(items[0]) # меч
# print(items[1]) # кирка
# print(items[2]) # яблоко

# items[0] = "алмазный меч"
# print(*items, sep=", ") # * распаковывает список, sep разделитель между элементами

'''Задание 1. Твой инвентарь
Создай список из пяти любимых игр. Выведи первую и третью игру, 
а затем замени вторую игру на "Minecraft" и выведи весь список.'''

# games = ['Roblox', 'GTA VI', 'Phasmophobia', 'Genshin Impact', 'CS Go']
# print(games[0])
# print(games[2])
# games[1] = "Minecraft"
# print(games)


"""Методы списка

Метод - это готовая команда, которая помогает что-то сделать со списком
"""

'''1. Метод .append() - добавить в конец'''

# items = ['меч', 'кирка']
#
# items.append('алмаз')
#
# print(items)


'''2. Метод .pop() - удалить по индексу или с конца списка по умолчанию'''

# items = ['меч', 'кирка', 'алмаз']

# items.pop(1)
# items.pop()
# print(items)


'''3. Метод .sort() - сортировка
sort() сортирует числа от меньшего к большему
и слова можно отсортировать по алфавиту
'''

# scores = [50, 10, 100, 30]
#
# scores.sort()
# print(scores)

# names = ['Саша', 'Анна', 'Тимофей', 'Илья']
# names.sort()
# print(names)

# alphabet = ['б', 'b', 'c', 'а']
# alphabet.sort()
# print(alphabet)

# numbers = [3, 1, 5, 2, 4]
# numbers.sort(reverse=True)
# print(numbers)


'''4. Метод .reverse() - перевернуть порядок
'''

# numbers = [1, 2, 3, 4, 5]
# numbers.reverse()
# print(numbers)

'''5. Метод .remove() - удалить по значению
'''

# items = ['меч', 'яблоко', 'кирка', 'яблоко']
# items.remove('яблоко')
# print(items)

'''6. Метод .insert() - вставить элемент в определенное место
'''

queue = ['Алекс', 'Маша', 'Дима', 'Саша']
print(queue)

queue.insert(1, 'Тимур')
print(queue)
