from turtle import Screen
from paddle import Paddle
from Ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=900, height=600)
screen.title("BongBong")
screen.tracer(0)

game_score = Score()

computer_paddle = Paddle()
my_paddle = Paddle(-390, 0)
my_ball = Ball()

screen.listen()
screen.onkeypress(lambda: my_paddle.move_paddle_up(), 'Up')
screen.onkeypress(lambda: my_paddle.move_paddle_down(), 'Down')

start_time = time.time()
hard_mode = False
while True:
  time.sleep(0.01)
  screen.update()
  
          
    
  my_ball.move()

  
  computer_paddle.auto_move_computer()
  
  if(hard_mode):
   if(my_ball.my_ball.ycor() < computer_paddle.ycor()):
         computer_paddle.setheading(270)
   elif(my_ball.my_ball.ycor()> computer_paddle.ycor()):
          computer_paddle.setheading(90)
   if time.time() - start_time >30 and game_score.my_score<game_score.computer_score:
          start_time = time.time()
          hard_mode = False
   
   
   computer_paddle.forward(3)
   
        

  if my_ball.my_ball.ycor() > 290 or my_ball.my_ball.ycor() < -290:
        my_ball.bounce_y()
        
  if my_ball.my_ball.xcor() > 445:
         game_score.my_score+=1
         my_ball.my_ball.home()
         game_score.write_score()
         hard_mode=True
         
         
  if my_ball.my_ball.xcor() < -445:
         game_score.computer_score+=1
         my_ball.my_ball.home()
         game_score.write_score()
         hard_mode=False
         
         
    

  if (my_ball.my_ball.distance(my_paddle) < 65 and my_ball.my_ball.xcor() < -370) or (my_ball.my_ball.distance(computer_paddle) < 65 and my_ball.my_ball.xcor() > 370):
        my_ball.bounce_x()
        
    
        

screen.exitonclick()
