import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.85,stretch_len=0.85)
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)





