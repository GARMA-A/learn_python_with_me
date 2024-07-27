from turtle import Turtle 

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270



class Snake:
       def __init__(self):
         self.snake_segmants =[]
         self.create_snake()
         self.pause = False
      
         self.head = self.snake_segmants[-1]
         
        
         
         
       def create_snake(self):
          for pos in STARTING_POSITIONS:
              self.add_segmant(pos)
              
              
       def extend_snake(self):
              self.add_segmant(self.snake_segmants[-1].position())

       def add_segmant(self,pos):
          new_segmant = Turtle('square')
          new_segmant.penup()
          new_segmant.color('white')
          new_segmant.goto(pos[0]-10,pos[1])
          self.snake_segmants.insert(0,new_segmant)
              
        
       def start_move(self):
        if not self.pause:
              for seg_num in range(len(self.snake_segmants)-1):   # size -1  becuse i will manually turn the head
                 new_x=self.snake_segmants[seg_num+1].xcor()
                 new_y=self.snake_segmants[seg_num+1].ycor()
                 self.snake_segmants[seg_num].goto(new_x,new_y)   
              self.head.forward(MOVE_DISTANCE)
         
       
      
       def move_right(self):
         if self.head.heading() != LEFT:
              self.snake_segmants[-1].setheading(RIGHT) 
               
       def move_up(self):
         if self.head.heading() != DOWN:
             self.snake_segmants[-1].setheading(UP)
             
       def move_left(self):
         if self.head.heading() != RIGHT:
              self.snake_segmants[-1].setheading(LEFT)
             
       def move_down(self):
         if self.head.heading() != UP:
             self.snake_segmants[-1].setheading(DOWN)
       def toggle_pause(self):
              self.pause = not self.pause;    
             
       
      
              
      
              
 

