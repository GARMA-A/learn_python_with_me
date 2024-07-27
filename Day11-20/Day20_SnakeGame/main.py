from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score_board
from random import *
from messages import Messages
import time

def __main__():
 SNAKE_SCREEN = Screen()
 game_is_on = True
 # SNAKE_SCREEN.resizemode('user')
 # SNAKE_SCREEN.shapesize(1,1,5)# height and width and borderRadius
 SNAKE_SCREEN.setup(width=600,height=600)
 SNAKE_SCREEN.title("Snake Game")
 SNAKE_SCREEN.bgcolor('black')
 SNAKE_SCREEN.tracer(0)
 SNAKE_SCREEN.listen()



 sn = Snake()
 msg = Messages()
 food = Food()
 score = Score_board()
 msg.stop_snake()
 while game_is_on:
           SNAKE_SCREEN.update()
           time.sleep(0.1)
           sn.start_move()
           SNAKE_SCREEN.onkey(sn.move_down , 'Down')
           SNAKE_SCREEN.onkey(sn.move_up , 'Up')
           SNAKE_SCREEN.onkey(sn.move_right , 'Right')
           SNAKE_SCREEN.onkey(sn.move_left ,'Left')   
           SNAKE_SCREEN.onkey(lambda: sn.toggle_pause() ,'p')   
           if sn.head.distance(food)<15:
             sn.extend_snake()
             score.current_score+=1
             score.write_score()
             food.refresh() 
           if sn.head.xcor() >= 310 or sn.head.xcor() <= -310 or sn.head.ycor() >= 310 or sn.head.ycor() <= -310:
              game_is_on = False
           for seg in sn.snake_segmants[:-1]: 
              if sn.head.distance(seg) < 10 :
                    game_is_on = False


 msg.write_gameover()  
 msg.write_quit()  
       
         
         
 SNAKE_SCREEN.onkey(lambda:SNAKE_SCREEN.bye(),'Escape')    
     
 SNAKE_SCREEN.exitonclick()



__main__()




















