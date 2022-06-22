import turtle
turtle.title("Italy Flag In Python")
s = turtle.getscreen()
t = turtle.Turtle()
t.pensize(10)
t.penup()

sp = input("Set speed to: ")
t.speed(int(sp))

t.fillcolor("green")
t.begin_fill()
t.goto(-240, 160)
t.pendown()
t.fd(480)
t.rt(90)
t.fd(320)
t.rt(90)
t.fd(480)
t.rt(90)
t.fd(320)
t.rt(90)

print("OUTLINE DONE")

t.end_fill()

print("GREEN FILL DONE")

t.fd(160)
t.fillcolor("white")
t.begin_fill()
t.fd(160)
t.rt(90)
t.fd(320)
t.rt(90)
t.fd(160)
t.rt(90)
t.fd(320)
t.rt(90)

print("WHITE OUTLINE DONE")

t.end_fill()

print("WHITE FILL DONE")

t.fd(160)
t.fillcolor("red")
t.begin_fill()
t.fd(160)
t.rt(90)
t.fd(320)
t.rt(90)
t.fd(160)
t.rt(90)
t.fd(320)
t.rt(90)

print("RED OUTLINE DONE")

t.end_fill()

print("RED FILL DONE")
print("END")

turtle.done()




