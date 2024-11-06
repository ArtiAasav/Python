 # 18
import turtle
import random



for i in range(6):
    d = random.randint(10,100)
    c = turtle.pencolor("black")
    #sein
    for i in range(4):
        turtle.fd(d)
        turtle.lt(90) 
    #uks
    turtle.penup()
    turtle.fd(d*0.25)
    turtle.pendown()
    c = turtle.pencolor("blue")
    for i in range(4):
        turtle.fd(d/2)
        turtle.lt(90)

    #katus
    turtle.penup()
    turtle.goto(0,d)
    turtle.lt(60)
    turtle.pendown()
    c = turtle.pencolor("green")
    for i in range(2):
        turtle.fd(d)
        turtle.rt(120)

    #järgmine maja
    turtle.penup()
    turtle.fd(d)
    turtle.lt(90)
    turtle.fd(d)
    turtle.lt(90)
    turtle.fd(d+20)
    turtle.pendown()







turtle.done()