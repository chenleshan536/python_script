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


#draw_square()
dot_count = 10000

dots_inside_circle = 0
t.speed(0)
t.penup()

for i in range(dot_count):
    x = random.uniform(-90,90)
    y = random.uniform(0,90)
    t.goto(x,y) 

    distance_to_center = math.sqrt(x**2 + y**2)

    if distance_to_center < 30 and distance_to_center > 20:
        #dots_inside_circle = dots_inside_circle+1          
        t.pencolor("red")
        t.dot(3)
    elif distance_to_center < 40 and distance_to_center > 30:
        #pass
        t.pencolor("orange")
        t.dot(3)
    elif distance_to_center < 50 and distance_to_center > 40:
        #pass
        t.pencolor("yellow")
        t.dot(3)
    elif distance_to_center < 60 and distance_to_center > 50:
        #pass
        t.pencolor("green")
        t.dot(3)
    elif distance_to_center < 70 and distance_to_center > 60:
        #pass
        t.pencolor("cyan")
        t.dot(3)
    elif distance_to_center < 80 and distance_to_center > 70:
        #pass
        t.pencolor("blue")
        t.dot(3)
    elif distance_to_center < 90 and distance_to_center > 80:
        #pass
        t.pencolor("purple")
        t.dot(3)
    elif distance_to_center < 0 and distance_to_center > 20:
        pass
    elif distance_to_center < 1000 and distance_to_center > 90:
        pass
    
    #t.dot(3)


#pi = 4 * dots_inside_circle / dot_count

#print("pi is ", pi)
