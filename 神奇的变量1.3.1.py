import turtle
turtle.bgcolor('white')
turtle.width(1)
sides = 4
colors=["red","orange","yellow","green","blue","purple"]
for x in range(60):
   turtle.pencolor(colors[x%sides])
   turtle.forword(x*2)
   turtle.left(360/sides+1)
