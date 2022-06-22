import turtle
turtle.title("Ireland Flag In Python")
s = turtle.getscreen()
t = turtle.Turtle()
t.pensize(10)
t.penup()

sp = input("Set speed to: ")
t.speed(int(sp))

t.fillcolor("orange")
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

print("ORANGE FILL DONE")

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
t.fillcolor("green")
t.begin_fill()
t.fd(160)
t.rt(90)
t.fd(320)
t.rt(90)
t.fd(160)
t.rt(90)
t.fd(320)
t.rt(90)

print("GREEN OUTLINE DONE")

t.end_fill()

print("GREEN FILL DONE")
print("END")

turtle.done()





