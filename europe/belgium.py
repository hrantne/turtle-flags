import turtle
turtle.title("Belgium Flag In Python (by Hrant)")
s = turtle.getscreen()
t = turtle.Turtle()
t.pensize(10)
t.penup()

sp = input("Set speed to: ")
t.speed(int(sp))

t.fillcolor("#333232")
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

print("BLACK FILL DONE")

t.fd(160)
t.fillcolor("yellow")
t.begin_fill()
t.fd(160)
t.rt(90)
t.fd(320)
t.rt(90)
t.fd(160)
t.rt(90)
t.fd(320)
t.rt(90)

print("YELLOW OUTLINE DONE")

t.end_fill()

print("YELLOW FILL DONE")

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


