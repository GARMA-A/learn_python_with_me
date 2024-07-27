from turtle import Turtle
class Score_board(Turtle):
       def __init__(self):
             super().__init__()
             self.current_score =0
             self.score =  Turtle()
             self.score.penup()
             self.score.color('white')
             self.score.hideturtle()
             self.score.goto(x=0,y=250)
             self.write_score()
             
             
       def update_score(self):
             
              self.current_score += 1
              self.write_score()
             
       
       def write_score(self): 
               self.score.clear() 
               self.score.write(f"Score : {self.current_score}",False,align='center',font=("Arial", 20, "normal")) 
       
   
          
             
              