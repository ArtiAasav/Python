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
turtle.goto(0,-150)
turtle.left(90)
turtle.fd(200)
turtle.rt(90)
turtle.begin_fill()
turtle.color("blue", "lightblue")
turtle.circle(70)
turtle.left(90)
turtle.end_fill()
turtle.begin_fill()
turtle.color("lightblue", "yellow")
turtle.fd(50)
turtle.end_fill()



turtle.done()