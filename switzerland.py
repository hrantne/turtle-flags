import turtle
turtle.title("Switzerland Flag In Python (by Hrant)")
s = turtle.getscreen()
t = turtle.Turtle()
t.pensize(10)
t.penup()

sp = input("Set speed to: ")
t.speed(int(sp))

t.goto(-150, 150)
t.pendown()
t.fillcolor("red")
t.begin_fill()

t.fd(300)
t.rt(90)
t.fd(300)
t.rt(90)
t.fd(300)
t.rt(90)
t.fd(300)
t.rt(90)

print("OUTLINE DONE")

t.end_fill()

print("RED FILL DONE")

t.penup()
t.pencolor("white")
t.fillcolor("white")
t.goto(-20, 75)
t.pendown()
t.begin_fill()

t.fd(40)
t.rt(90)
t.fd(150)
t.rt(90)
t.fd(40)
t.rt(90)
t.fd(150)
t.rt(90)

print("CROSS 1 OUTLINE DONE")

t.end_fill()

print("WHITE FILL DONE")

t.penup()
t.goto(-75, 20)
t.pendown()
t.begin_fill()

t.fd(150)
t.rt(90)
t.fd(40)
t.rt(90)
t.fd(150)
t.rt(90)
t.fd(40)
t.rt(90)

print("CROSS 2 OUTLINE DONE")

t.end_fill()

print("WHITE FILL DONE")

turtle.done()
