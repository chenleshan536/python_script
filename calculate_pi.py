import turtle
import random
import math

t = turtle

def draw_square():
    t.forward(200)
    print(t.position())
    t.left(90)
    t.forward(200)
    print(t.position())
    t.left(90)
    t.forward(200)
    print(t.position())
    t.left(90)
    t.forward(200)
    print(t.position())    
    t.left(90)


draw_square()
dot_count = 10000000

dots_inside_circle = 0
t.speed(0)
t.penup()

for i in range(dot_count):
    x = random.uniform(0,200)
    y = random.uniform(0,200)
    #t.goto(x,y) 

    distance_to_center = math.sqrt((x-100)**2 + (y-100)**2)

    if distance_to_center < 100:
        dots_inside_circle = dots_inside_circle+1          
        #t.pencolor("red")
    else:
        pass
        #t.pencolor("blue")

    
    #t.dot()


pi = 4 * dots_inside_circle / dot_count

print("pi is ", pi)
        

    
