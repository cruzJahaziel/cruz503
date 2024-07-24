from turtle import *
from math import *

speed(-1000)
bgcolor("black")
goto(0,-40)

for i in range(16):
    for j in range(18):
        color('#FFA216')
        rt(90)
        circle(150-j*6, 90)
        lt(90)
        circle(150-j*6, 90)
        rt(100)
    circle(40, 24)

color('black')
shape('circle')
shapesize(0.5)
fillcolor('#884513')
golden_ang=137.508
phi = golden_ang*(pi/100)

for i in range(140):
    r = 4*sqrt(i)
    theta = i*phi
    x = r*cos(theta)
    y = r*sin(theta)
    penup()
    goto(x, y)
    setheading(i*golden_ang)
    pendown()
    stamp()

def circulo(x, y):
    penup()
    goto(x, y)
    pendown()
    color('red')
    fillcolor('black')
    begin_fill()
    circle(3)
    end_fill()

def dibujar_L(x, y):
    pos_l = [(x, y), (x, y+4), (x, y+8), (x, y+12), (x, y+16), (x, y+20), (x, y+24), (x+4, y)]
    for pos in pos_l:
        circulo(*pos)

def dibujar_O(x, y):
    pos_o = [(x, y), (x, y+4), (x, y+8), (x, y+12), (x, y+16), (x, y+20), (x, y+24),
             (x+4, y), (x+4, y+24), (x+8, y), (x+8, y+24), (x+12, y), (x+12, y+24),
             (x+16, y), (x+16, y+24), (x+20, y), (x+20, y+24), (x+24, y), (x+24, y+4),
             (x+24, y+8), (x+24, y+12), (x+24, y+16), (x+24, y+20), (x+24, y+24)]
    for pos in pos_o:
        circulo(*pos)

def dibujar_V(x, y):
    pos_v = [(x, y), (x+2, y-4), (x+4, y-8), (x+6, y-12), (x+8, y-16), (x+10, y-20),
             (x+12, y-24), (x+14, y-20), (x+16, y-16), (x+18, y-12), (x+20, y-8), 
             (x+22, y-4), (x+24, y)]
    for pos in pos_v:
        circulo(*pos)

def dibujar_E(x, y):
    pos_e = [(x, y), (x, y+4), (x, y+8), (x, y+12), (x, y+16), (x, y+20), (x, y+24),
             (x+4, y), (x+8, y), (x+12, y), (x+16, y), (x+20, y), (x+24, y),
             (x+4, y+12), (x+8, y+12), (x+12, y+12), (x+16, y+12), (x+20, y+12), (x+24, y+12),
             (x+4, y+24), (x+8, y+24), (x+12, y+24), (x+16, y+24), (x+20, y+24), (x+24, y+24)]
    for pos in pos_e:
        circulo(*pos)

# Llamadas a las funciones para dibujar "LOVE"
dibujar_L(-100, 0)
dibujar_O(-50, 0)
dibujar_V(0, 0)
dibujar_E(50, 0)

hideturtle()
done()
