from turtle import *

def draw_square(length,color):
    pencolor(color)
    for _ in range(4):
        forward(length)
        left(90)

# draw_square(100,'blue')

# mainloop()