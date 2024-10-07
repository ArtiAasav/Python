# Arti Aasav
# 04.10.2024
# Harjutus 02 olümpiarõngad

import turtle
 
aken = turtle.Screen()
aken.setup(width=500, height=400)
aken.title("Olümpiarõngad - Arti")
turtle.speed(0)
turtle.pensize(6)
 
#olümpiarõngad
#sinine
turtle.penup()
turtle.goto(-120,-20)
turtle.pendown()
turtle.pencolor("blue")
turtle.circle(50)

#must
turtle.penup()
turtle.goto(0,-20)
turtle.pendown()
turtle.pencolor("black")
turtle.circle(50)

#punane
turtle.penup()
turtle.goto(120,-20)
turtle.pendown()
turtle.pencolor("red")
turtle.circle(50)

#kollane
turtle.penup()
turtle.goto(-60,-60)
turtle.pendown()
turtle.pencolor("yellow")
turtle.circle(50)

#roheline
turtle.penup()
turtle.goto(60,-60)
turtle.pendown()
turtle.pencolor("green")
turtle.circle(50) 
 
 
 
turtle.done()