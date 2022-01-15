import turtle
t=turtle
t.pencolor("red")
t.speed(5)
for i in range(1,31):
    t.forward(i*3)
    t.left(90)
t.penup()
t.goto (2,0)
t.right(180)
t.pendown()
for i in range(1,31):
    t.forward(i*3)
    t.left(90)
t.penup()
t.goto (0,-2)
t.right(180)
t.pendown()
for i in range(1,31):
    t.forward(i*3)
    t.left(90)
    t.penup()
t.goto (0,2)
t.right(180)
t.pendown()
for i in range(1,31):
    t.forward(i*3)
    t.left(90)
    t.penup()
t.goto (-2,0)
t.right(180)
t.pendown()
for i in range(1,31):
    t.forward(i*3)
    t.left(90)
