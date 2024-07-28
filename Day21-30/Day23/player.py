from turtle import Turtle

MOVE_DESTANCE = 10

class Player(Turtle):
       
       def __init__(self):
              super().__init__()
              self.shape('turtle')
              self.color('gray70')
              self.penup()
              self.goto(0 , -270)
              self.setheading(90)
       def move_up(self):
              self.forward(MOVE_DESTANCE)
                       
              
              
              