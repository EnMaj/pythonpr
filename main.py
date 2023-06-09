from turtle import *
import turtle

color("blue")
begin_fill()
penup()
goto(100,0)
for i in range(4):
    forward(100)
    right(90)
end_fill()

color("yellow")
begin_fill()
goto(150,-150)
circle(25)
end_fill()

color("yellow")
begin_fill()
penup()
goto(125,25)
for i in range(2):
    forward(50)
    right(90)
    forward(25)
    right(90)
end_fill()

color('red')
begin_fill()
penup()
goto(125,25)
for i in range(3):
    forward(50)
    lt(120)
end_fill()

color("yellow")
begin_fill()
penup()
goto(200,50)
for i in range(2):
    forward(75)
    right(90)
    forward(150)
    right(90)
end_fill()

color('green')
begin_fill()
penup()
goto(225,50)
for i in range(3):
    forward(25)
    lt(120)
end_fill()

color("green")
begin_fill()
goto(238,-140)
circle(35)
end_fill()

color("blue")
begin_fill()
penup()
goto(220,20)
for i in range(4):
    forward(40)
    right(90)
end_fill()

color("red")
begin_fill()
penup()
goto(275,0)
for i in range(4):
    forward(100)
    right(90)
end_fill()

color("green")
begin_fill()
penup()
goto(320,100)
for i in range(2):
    forward(40)
    right(90)
    forward(100)
    right(90)
end_fill()

color("blue")
begin_fill()
goto(325,-140)
circle(48)
end_fill()

color("yellow")
begin_fill()
goto(300,100)
circle(25)
end_fill()

color("yellow")
begin_fill()
goto(250,135)
circle(30)
end_fill()

color("yellow")
begin_fill()
goto(170,150)
circle(40)
end_fill()

color("red")
begin_fill()
penup()
goto(0,-25)
for i in range(2):
    forward(100)
    right(90)
    forward(20)
    right(90)
end_fill()

def triangle(a):
    for i in range(3):
        t.forward(a)
        t.left(120)


def square(a):
    for i in range(4):
        t.forward(a)
        t.right(90)


def circle(a):
    t.circle(a)


def rhombus(a):
    for i in range(2):
        t.forward(a)
        t.left(60)
        t.forward(a)
        t.left(120)


t = turtle.Turtle()
w = turtle.Screen()

t.penup()
t.right(90)
t.forward(20)
t.pendown()
t.color('green')
t.begin_fill()
square(80)
t.end_fill()
t.right(150)
t.color('red')
t.begin_fill()
triangle(70)
t.end_fill()
t.left(60)
t.forward(70)
t.right(120)
t.color('blue')
t.begin_fill()
triangle(70)
t.end_fill()
t.forward(70)
t.penup()
t.right(60)
t.forward(10)
t.left(120)
t.pendown()
t.color('yellow')
t.begin_fill()
triangle(70)
t.end_fill()
t.penup()
t.left(60)
t.forward(15)
t.left(90)
t.forward(140)
t.right(90)
t.color('blue')
t.begin_fill()
circle(30)
t.end_fill()
t.penup()
t.forward(60)
t.pendown()
t.color('yellow')
t.begin_fill()
square(100)
t.end_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.color('blue')
t.begin_fill()
rhombus(60)
t.end_fill()
t.forward(50)
t.penup()
t.right(90)
t.forward(100)
t.right(90)
t.pendown()
t.color('green')
t.begin_fill()
circle(30)
t.end_fill()
t.penup()
t.forward(60)
t.pendown()
t.color('blue')
t.begin_fill()
square(80)
t.end_fill()
t.right(90)
t.forward(80)
t.left(90)
t.forward(5)
t.right(60)
t.color('green')
t.begin_fill()
triangle(70)
t.end_fill()
t.left(60)
t.forward(35)
t.left(90)
t.penup()
t.forward(80)
t.pendown()
t.right(90)
t.color('yellow')
t.begin_fill()
circle(30)
t.end_fill()

w.mainloop()
