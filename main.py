# item1 = "Меч"
# item2 = "Кирка"
# item3 = "Яблоко"
# item4 = "Алмаз"
# item5 = "Щит"
#
# inventory = ["Меч", "Кирка", "Яблоко", "Алмаз", "Щит"]

"""Коллекция - это структура данных, которая позволяет хранить несколько значений вместе
и удобно с ними работать!"""

"""Список"""

# inventory = ["Меч", 'Яблоко', 'Алмаз']    # внутри списка только строки
# scores = [100, 250, 80]                   # внутри списка только числа
# mixed = ["Steve", 100, True]              # внутри списка и строка и число и логический тип данных
# empty = []                                # внутри списка ничего нет - пустой список

# inventory = ["Меч", 'Яблоко', 'Алмаз', "Щит"]
# print(inventory[0])
# print(inventory[2])
# print(inventory[-1])
# print(len(inventory))

'''Методы списка'''

# 1. Метод .append() - добавляем предмет. Всегда добавляет один элемент в конец списка
# inventory = ['Меч', 'Яблоко']
# inventory.append('Алмаз')
# inventory.append('Щит')
# print(inventory)

# 2. Метод .pop() - выбрасываем предмет.
# inventory = ['Меч', 'Яблоко', 'Алмаз']
# inventory.pop()
# print(inventory)

# 3. Метод .insert() - вставляем на нужное место.

# heroes = ['Бэтмен', 'Железный человек']
# heroes.insert(1, "Человек паук")
# print(heroes)

# 4. Метод .remove() - удаляем конкретный элемент.
# inventory = ['Меч', 'Яблоко', 'Алмаз']
# inventory.remove("Яблоко")
# print(inventory)

# 5. Метод .reverse() - переворачиваем порядок.
# race = ['Макс', 'Алекс', 'Саша']
# race.reverse()
# print(race)

# 6. Метод .sort() - сортируем
# scores = [500, 100, 900, 250, 700]
# scores.sort()
# scores.sort(reverse=True)
# print(scores)

# names = ['Zara', 'Alex', 'Mike']
# names.sort()
# print(names)

names = ['Юлия', 'Александр', 'София', 'Zara', 'Mike', 'Alex']
names.sort()
print(names)
