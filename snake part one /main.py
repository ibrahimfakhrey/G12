import time
from turtle import Turtle,Screen

def up():
    if all_segments[0].heading() != 270:
        all_segments[0].setheading(90)

def down():
    if all_segments[0].heading() != 90:
        all_segments[0].setheading(270)
def left():
    if all_segments[0].heading() != 0:
        all_segments[0].setheading(180)
def right():
    if all_segments[0].heading() != 180:
        all_segments[0].setheading(0)
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake Game ")
screen.tracer(0)
screen.listen()
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(left,"Left")
screen.onkey(right,"Right")


positions=[(0,0),(-20,0),(-40,0)]
all_segments=[]
for p in positions:
    new_seg=Turtle("square")
    new_seg.penup()
    new_seg.color("white")
    new_seg.goto(p)

    all_segments.append(new_seg)

while True:
    time.sleep(0.1)
    screen.update()

    for i in range (len(all_segments)-1,0,-1):
        new_x=all_segments[i-1].xcor()
        new_y=all_segments[i-1].ycor()
        all_segments[i].goto(new_x,new_y)
    all_segments[0].forward(10)











screen.exitonclick()