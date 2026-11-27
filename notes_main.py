from mcpi.minecraft import Minecraft

mc = Minecraft.create()

password = input("Введите секретный пароль: ")

if password == "777":
    x, y, z = mc.player.getTilePos()
    x = x + 10

    # Алмазное основание
    mc.setBlocks(x, y - 1, z,
                 x + 14, y - 1, z + 14, 57)

    # Золотые стены
    mc.setBlocks(x, y, z,
                 x + 14, y + 7, z + 14, 41)

    # Освобождаем пространство внутри
    mc.setBlocks(x + 1, y, z + 1,
                 x + 13, y + 6, z + 13, 0)

    # Стеклянная крыша
    mc.setBlocks(x + 1, y + 7, z + 1,
                 x + 13, y + 7, z + 13, 20)

    # Большой вход
    mc.setBlocks(x+5, y, z,
                 x+9, y+4, z, 0)

    # Изумрудный пьедестал
    mc.setBlocks(x+5, y, z+5,
                 x+9, y+1, z+9, 133)

    # Алмазное сокровище
    mc.setBlocks(x+6, y+2, z+6,
                 x+8, y+3, z+8, 57)

    # Освещение
    mc.setBlocks(x+1, y+6, z+1,
                 x+13, y+6, z+1, 89)

    mc.postToChat("Сокровище разблокировано!")
