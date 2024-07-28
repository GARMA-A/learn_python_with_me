from turtle import Turtle

class Score(Turtle):
       def __init__(self):
              self.my_score = 0
              self.computer_score = 0
              self.msg = Turtle()
              self.msg.penup()
              self.msg.color("white")
              self.msg.hideturtle()
              self.msg.color('LimeGreen')
              self.msg.goto(-65,230)
              self.write_score()
       
       def write_score(self):
              self.msg.clear()
              self.msg.write(f"{self.my_score} : {self.computer_score}" , False,font=("Arial", 42, "bold"))  