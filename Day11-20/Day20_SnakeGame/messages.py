from turtle import Turtle

class Messages(Turtle):
       
       def __init__(self):
             self.current_msg =0
             self.msg =  Turtle()
             self.msg.penup()
             self.msg.hideturtle()
       
       
       def write_gameover(self):
               self.msg.goto(x=0,y=100)
               self.msg.color('red')
               self.msg.write(f"Game Over",False,align='center',font=("Arial", 26, "bold")) 
       
       def write_quit(self):
               self.msg.goto(x=0,y=-50)
               self.msg.color('LimeGreen')
               self.msg.write("To quit press Escape or click on screen",False,align='center',font=("Arial", 18, "normal")) 
       
       def stop_snake(self):
              self.msg.goto(x=200,y=-250)
              self.msg.color('LimeGreen')
              self.msg.write("press 'p' to puse",False,align='center',font=("Arial", 10, "normal")) 
   
              