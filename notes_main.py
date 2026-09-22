import pickle

from mcpi.minecraft import Minecraft
mc = Minecraft.create()


# Сортировка координат
def sort(n1, n2):
    if n1 > n2:
        return n2, n1
    else:
        return n1, n2


# Копирование конструкции
def copy_structure(x1, y1, z1, x2, y2, z2):
    # Сортируем координаты
    x1, x2 = sort(x1, x2)
    y1, y2 = sort(y1, y2)
    z1, z2 = sort(z1, z2)

    # Определяем размеры конструкции
    width = x2 - x1
    height = y2 - y1
    length = z2 - z1

    # Создаем список для конструкции
    structure = []

    print("Пожалуйста, подождите...")

    # Копируем все блоки конструкции
    for column in range(height):
        structure.append([])

        for row in range(width):
            structure[column].append([])

            for depth in range(length):
                block = mc.getBlockWithData(
                    x1 + row,
                    y1 + column,
                    z1 + depth
                )

                structure[column][row].append(block)

    return structure


# Получаем координаты первого угла
input("Пройдите к первому углу и нажмите Enter в этом окне")
x1, y1, z1 = mc.player.getTilePos()


# Получаем координаты противоположного угла
input("Пройдите к противоположному углу и нажмите Enter в этом окне")
x2, y2, z2 = mc.player.getTilePos()


# Копируем конструкцию
print("Копируем в файл")

structure = copy_structure(
    x1, y1, z1,
    x2, y2, z2
)


# Сохраняем конструкцию в файл
file = open("structure.txt", "wb")
pickle.dump(structure, file)
file.close()

print("Конструкция сохранена!")
