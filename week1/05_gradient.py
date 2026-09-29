import turtle
from random import random

CANVAS_W = 1000
CANVAS_H = 1000

screen = turtle.Screen()
screen.setup(CANVAS_W, CANVAS_H)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed()

num_rows = 4
num_cols = 4
start_x = -CANVAS_W / 2
start_y = CANVAS_H / 2

cell_w = CANVAS_W / num_cols
cell_h = CANVAS_H / num_rows

# Два цвета
color_a = (1,0,0)
color_b =(0.16, 0.2, 0.36)

# функция которая позволяет нам скользить от а до б, регулирую коэффициент к
# К от нуля до единицы. Если к = 0, то мы остаемся в точке а, если к = 1, то мы оказываемся в точке б. 
# Если к = 0,5, то мы на середине пути между а и б
def mix(a,b,k):
    return a + (b - a)*k

# Функция которая берет 2 цвета и в зависимости от параметра к мы оказываемся
# в другом цвете. если к=0, то мы в цвете 1
# если к=1 то мы в цвете 2
# если к=0.5 то мы посередине между двумя цветами 
def between(color1, color2, k):
    r = mix(color1[0], color2[0], k)
    g = mix(color1[1], color2[1], k)
    b = mix(color1[2], color2[2], k)
    return (r,g,b)


# Функция для ячейки
def cell(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.pencolor(color)

    t.begin_fill()
    for i in range(2):
        t.forward(cell_w)
        t.right(90)
        t.forward(cell_h)
        t.right(90)
    t.end_fill()

num_cells = num_cols * num_rows

for i in range(num_cells):
    row = i // num_cols
    col = i % num_cols

    # k = (row + col) % 2
    # k = row / (num_rows -1) градиент
    k = col / (num_cols - 1)

    x = start_x + col * cell_w
    y = start_y - row * cell_h

    color = between(color_a, color_b, k)
    cell(x, y, color)

screen.update()
screen.exitonclick()