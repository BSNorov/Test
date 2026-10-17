import turtle                           # всегда в начале строк: подключаем (импортируем) модуль turtle

t = turtle.Pen()

# t.color("red")      # меняет цвет пера

'''Квадрат'''
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)


'''Треугольник'''
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)

'''Круг'''
# t.circle(100)



'''Закрашенный квадрат
begin_fill()
между ними тут будет рисунок
end_fill()

'''
# t.color("blue")
# t.begin_fill()
# for i in range(4):
#     t.forward(100)
#     t.left(90)

# t.end_fill()

t.penup()                   # Команда не рисует
t.goto(70, 50)        # Двигается по точка, сначала x, а потом y
t.pendown()                 # Команда рисует
t.forward(100)


turtle.mainloop()                       # всегда в конце кода
