from turtle import Screen
from player import Player
from car_manager import Car_manager
from messages import Messages
import time

my_screen = Screen()
my_screen.tracer(0)

my_player = Player()
my_cars = Car_manager()
my_message = Messages()


my_screen.bgcolor("black")
my_screen.setup(width=900, height=600)
my_screen.title("Cross the road")
my_screen.listen()




       
       
       
def __main__(): 
 game_is_on = True 
       
 def restart():
       game_is_on = True
       my_player.goto(0 , -270)
       my_message.clear_all()
       my_cars.remove_cars()
       my_message.score = 1
       my_cars.cars=[]
       my_cars.cars_speed = 0
       my_message.write_score_msg()
       __main__()
 while game_is_on:
   time.sleep(0.1)
   my_screen.update()
   my_cars.create_car()
   my_cars.move_cars()
  
   for car in my_cars.cars:
    if car.distance(my_player)<25:
         game_is_on = False
         my_message.write_game_over()
         my_message.write_play_again()
         
   if my_player.ycor()>=290:
         my_player.goto(0,-290)
         my_message.score+=1
         my_message.write_score_msg()
         my_cars.cars_speed+=0.5
   my_screen.onkeypress(my_player.move_up,'Up')
   

 
 my_screen.onkey(my_screen.bye,'Escape')
 
 my_screen.onkey(restart , 'r')
 my_screen.mainloop()

__main__()


