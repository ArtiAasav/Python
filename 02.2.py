# Arti Aasav
# 04.10.2024
# Harjutus 02.2 Sinilill

import turtle
 
aken = turtle.Screen()
aken.setup(width=500, height=500)
aken.title("Sinilill - Arti")
turtle.speed(0)
turtle.pensize(10)

#Sinilill
turtle.pencolor("green")
turtle.goto(0,-100)
turtle.left(90)
turtle.fd(200)
turtle.rt(90)
turtle.begin_fill()
turtle.color("blue", "lightblue")
turtle.circle(70)
turtle.end_fill()
turtle.penup()
turtle.lt(90)
turtle.fd(40)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow", "yellow")
turtle.rt(90)
turtle.circle(30)
turtle.end_fill()

#Leht
turtle.penup()
turtle.goto(-20,0)
turtle.pendown()
turtle.begin_fill()
turtle.color("green", "green")
turtle.lt(90)
turtle.fd(40)
turtle.left(120)
turtle.fd(40)
turtle.left(120)
turtle.fd(40)
turtle.left(120)
turtle.end_fill()

turtle.done()