import random
import time
from turtle import Turtle ,Screen


screen=Screen()
screen.setup(width=600,height=700)
screen.bgcolor("black")

poistions=[(-288,0),(-288,30),(-288,50)]
colors=["red","green","blue"]
c=0
all_turtles=[]
for i in poistions:
    tim=Turtle("turtle")
    tim.color(colors[c])
    c+=1
    tim.penup()
    tim.goto(i)
    all_turtles.append(tim)
game_is_on=True
user_input = screen.textinput(title="Make a Prediction", prompt="Write your favorite color:")
while game_is_on:

    for turtle in all_turtles:
        if turtle.xcor() >280:
            game_is_on = False
            if user_input==turtle.pencolor():
                screen.textinput("Game Result", "you won")
            else:
                screen.textinput("Game Result", "you lose")

        else:
            turtle.forward(random.randint(20,40))
screen.exitonclick()