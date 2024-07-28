from turtle import Turtle
from typing import Any

COLORS = ['SpringGreen2','OrangeRed1','red2']

class Messages(Turtle):
       
       def __init__(self):
              super().__init__()
              self.score = 1
              self.create_score_msg()
              self.write_score_msg()
              self.create_game_over()
              self.create_play_again()
              
       
       
       def create_score_msg(self):
              self.score_msg = Turtle()
              self.score_msg.goto(x=-400 , y=250)
              self.score_msg.hideturtle()
              self.score_msg.penup()
             
              
       
       def write_score_msg(self):
              self.score_msg.clear()
              if self.score>3:
                self.score_msg.color(COLORS[1])
              elif self.score>7:
                self.score_msg.color(COLORS[2])
              else :
                self.score_msg.color(COLORS[0])
              self.score_msg.write(f'Level : {self.score}' , False , font=("Arial", 20, "bold"))  
              
       def create_game_over(self):
              self.game_over = Turtle()
              self.game_over.hideturtle()
              self.game_over.penup()
              self.game_over.goto(x=-100 ,y=0)
              self.game_over.color('red1')
              
              
       
       def write_game_over(self):
              self.game_over.clear()
              self.game_over.write("Game Over" , False , font=("Arial", 28, "bold")) 
       
       def create_play_again(self):
              self.play_again= Turtle()
              self.play_again.hideturtle()
              self.play_again.penup()
              self.play_again.goto(x=-110 ,y=-50)
              self.play_again.color('MediumSpringGreen')
              
       def write_play_again(self):
              self.play_again.clear()
              self.play_again.write("To play again press 'R'" , False , font=("Arial", 16, "bold")) 
              
       def clear_all(self):
              self.game_over.clear()
              self.play_again.clear()
              self.score_msg.clear()
              
              
              
              
              
       
              