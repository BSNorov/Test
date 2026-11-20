# from mcpi.minecraft import Minecraft
#
# mc = Minecraft.create()
#
# pos = mc.player.getPos()
#
# x = pos.x
# y = pos.y
# z = pos.z
#
# print("X =", x)
# print("Y =", y)
# print("Z =", z)
#
# print("Тип координаты X:", type(x))
#
# mc.postToChat("GPS активирован!")

import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z

time.sleep(3)

mc.postToChat("Телепорт 1!")

mc.player.setTilePos(x + 5, y + 1, z)

time.sleep(3)

mc.postToChat("Телепорт 2!")
mc.player.setTilePos(x + 5.5, y + 1, z + 5.5)
