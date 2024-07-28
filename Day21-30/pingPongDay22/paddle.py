from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x=390, y=0):
        super().__init__()
        self.create_new_paddle(x, y)
            
    def create_new_paddle(self, x, y):
        self.shape('square')
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.setheading(90)
        self.shapesize(1, 5, 3)
       
    def move_paddle_up(self):
        if self.ycor() < 240:
            newy = self.ycor() + 20
            self.goto(self.xcor(), newy)
       
    def move_paddle_down(self):
        if self.ycor() > -240:
            newy = self.ycor() - 20
            self.goto(self.xcor(), newy)
            
    def auto_move_computer(self):
       if self.ycor() >= 275:
            self.setheading(270)  
       elif self.ycor() <= -275:
             self.setheading(90) 
         
