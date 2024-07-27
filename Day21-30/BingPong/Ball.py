from turtle import Turtle

class Ball:
    def __init__(self):
        self.create_ball()
        self.direction = "up_right"
              
    def create_ball(self):
        self.my_ball = Turtle()
        self.my_ball.shape('circle')
        self.my_ball.color('white')
        self.my_ball.penup()
          
    def move(self , x=3 , y=3):    
        xcor = self.my_ball.xcor()
        ycor = self.my_ball.ycor()
        if self.direction == "up_right":
            self.my_ball.goto(xcor + x, ycor + y)
        elif self.direction == "down_right":
            self.my_ball.goto(xcor + x, ycor - y)
        elif self.direction == "up_left":
            self.my_ball.goto(xcor - x, ycor + y)
        elif self.direction == "down_left":
            self.my_ball.goto(xcor - x, ycor - y)
              
    def bounce_y(self):
        if self.direction == "up_right":
            self.direction = "down_right"
        elif self.direction == "down_right":
            self.direction = "up_right"
        elif self.direction == "up_left":
            self.direction = "down_left"
        elif self.direction == "down_left":
            self.direction = "up_left"
              
    def bounce_x(self):
        if self.direction == "up_right":
            self.direction = "up_left"
        elif self.direction == "down_right":
            self.direction = "down_left"
        elif self.direction == "up_left":
            self.direction = "up_right"
        elif self.direction == "down_left":
            self.direction = "down_right"
