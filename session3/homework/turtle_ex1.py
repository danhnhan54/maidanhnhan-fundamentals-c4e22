from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
a = 3
for i in colors:
    color(i)
    for i in range(a):
        forward(100)
        left(360/a)
    a += 1


mainloop()