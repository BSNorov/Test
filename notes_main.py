# Целые числа
# gold = 6
# hp = 100
# price = 60


# Вещественные числа (дробные или числа с плавающей точкой)
# half_apple = 0.5
# distance = 100.55

# print(gold)
# print(hp)
# print(half_apple)
# print(distance)

'''Закомментировать (отключить) код можно с помощью комбинации Ctrl / 
У кого MacOS - Cmnd /'''

from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

# Получаем позицию игрока
pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z

# Целое число
height = 6

# Вещественное число
distance = 8.5

# Строим первую башню
mc.setBlocks(
    x + 2, y, z,
    x + 2, y + height, z,
    block.GOLD_BLOCK.id
)

# Строим вторую башню
mc.setBlocks(
    x + 7, y, z,
    x + 7, y + 3, z,
    block.DIAMOND_BLOCK.id
)

# Показываем значения
mc.postToChat("Высота = " + str(height))
mc.postToChat("Расстояние = " + str(height))
