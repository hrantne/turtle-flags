import turtle
turtle.title("Yemen Flag In Python")
s = turtle.getscreen()
t = turtle.Turtle()
t.pensize(10)
t.penup()

sp = input("Set speed to: ")
t.speed(int(sp))

t.fillcolor("red")
t.begin_fill()
t.goto(-240, 160)
t.pendown()
t.fd(480)
t.rt(90)
t.fd(330)
t.rt(90)
t.fd(480)
t.rt(90)
t.fd(330)
t.rt(180)

print("OUTLINE DONE")

t.end_fill()

print("RED FILL DONE")

t.fd(110)
t.fillcolor("white")
t.begin_fill()
t.lt(90)
t.fd(480)
t.rt(90)
t.fd(110)
t.rt(90)
t.fd(480)
t.rt(90)
t.fd(110)
t.rt(180)

print("WHITE OUTLINE DONE")

t.end_fill()

print("WHITE FILL DONE")

t.fd(220)
t.fillcolor("black")
t.begin_fill()
t.lt(90)
t.fd(480)
t.lt(90)
t.fd(110)
t.lt(90)
t.fd(480)

print("BLACK OUTLINE DONE")

t.end_fill()

print("BLACK FILL DONE")
print("END")

turtle.done()





