from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0)]
MOVE_DESTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
       def __init__(self):
              self.segments = []
              self.create_snake()
       def create_snake(self):
              for position in STARTING_POSITIONS:
                new_segmant = Turtle('square')
                new_segmant.color("white")
                new_segmant.penup()
                new_segmant.goto(position)
                self.segments.append(new_segmant)
       def move(self):
          for seg_num in range(len(self.segments)-1 , 0 , -1):
              new_x = self.segments[seg_num-1].xcor()
              new_y = self.segments[seg_num-1].ycor()
              self.segments[seg_num].goto(new_x,new_y)
              self.segments[0].forward(MOVE_DESTANCE)
       def left(self):
              if(self.segments[0].heading()!=RIGHT):
                self.segments[0].setheading(LEFT)
       def right(self):
              if(self.segments[0].heading()!=LEFT):
                self.segments[0].setheading(RIGHT)
       def up(self):
              if(self.segments[0].heading()!=DOWN):
                self.segments[0].setheading(UP)
       def down(self):
               if(self.segments[0].heading()!=UP):
                self.segments[0].setheading(DOWN)
      
       
              
              