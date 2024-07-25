from turtle import  Screen
import time
from snake import Snake
import  food 
  



screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()









screen.update()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
       
       
game_is_on = True

while game_is_on:
       screen.update()
       snake.move()
       time.sleep(0.1)
       if snake.head.distance(food) <15:
              food.refresh()
       
              
              


















screen.exitonclick()