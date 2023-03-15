from turtle import *

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