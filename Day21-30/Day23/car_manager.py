from turtle import Turtle
import random
MOVE_DESTANCE = 10

COLORS = ['red','green','blue','yellow',"DarkOrchid","MistyRose2","LightSteelBlue2"]

class Car_manager(Turtle):
       
       def __init__(self):
              super().__init__()
              self.cars = []
              self.cars_speed = 0
       
       
       def create_car(self):
            choice = random.randint(0,5)
            if self.cars_speed>2:
                  choice = random.randint(1,2)
            elif self.cars_speed>1:
                   choice = random.randint(1,3)
           
            if choice ==1:  
              new_car = Turtle('square')
              new_car.resizemode('user')
              new_car.shapesize(1,2,10)
              new_car.color(random.choice(COLORS))
              new_car.penup()
              new_car.goto(450 , random.randint(-210,210))
              self.cars.append(new_car)
              
       def move_cars(self):
              for car in self.cars:
                     car.backward(MOVE_DESTANCE+self.cars_speed)
       
       def remove_cars(self):
               for car in self.cars:
                      car.hideturtle()
              