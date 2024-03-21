# your task is to make the class of the food it should be a circle with a blue color
# and it appears in a random place in the screen
#and when the snake make colosion with the food it dis appear and appears in another place

# ths snake if it touch any screen game stops
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)
        self.goto(random_x,random_y)
