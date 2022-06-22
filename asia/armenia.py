import turtle
turtle.title("Armenia Flag In Python")
s = turtle.getscreen()
t = turtle.Turtle()
t.pensize(10)
t.penup()

sp = input("Set speed to: ")
t.speed(int(sp))

t.goto(-200, 300)
t.pendown()

t.fillcolor("red")
t.begin_fill()

t.fd(400)
t.rt(90)
t.fd(150)
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(150)
t.rt(180)

print("OUTLINE DONE")

t.end_fill()

print("RED DONE")

t.fillcolor("blue")
t.begin_fill()

t.fd(300)
t.lt(90)
t.fd(400)
t.lt(90)
t.fd(150)
t.lt(90)
t.fd(400)

t.end_fill()

print("BLUE DONE")

t.fillcolor("orange")
t.begin_fill()

t.lt(90)
t.fd(300)
t.lt(90)
t.fd(400)
t.lt(90)
t.fd(150)
t.lt(90)
t.fd(400)

t.end_fill()

print("ORANGE DONE")
print("END")

turtle.done()
