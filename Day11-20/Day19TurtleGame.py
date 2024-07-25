from turtle import Turtle , Screen
import random


# new_Turtle = Turtle()
# screen = Screen()

# def move_forwards():
#        new_Turtle.forward(10)
# def move_backward():
#        new_Turtle.backward(10)
# def turn_Right():
#        new_Turtle.right(60)
# def turn_left():
#        new_Turtle.left(60)
# def go_home():
#        new_Turtle.clear()



# screen.onkey(key="Up", fun=move_forwards)
# screen.onkey(key="Down", fun=move_backward)
# screen.onkey(key="Left", fun=turn_left)
# screen.onkey(key="Right", fun=turn_Right)
# screen.onkey(key="e", fun=go_home)
# screen.exitonclick()
# /************************************************/
# /************************************************/
# /************************************************/


def display_message(user_bet , curTurtleColor):
    message_turtle = Turtle()
    message_turtle.hideturtle() 
    message_turtle.penup()  
    message_turtle.goto(0, 0)  
    if(user_bet.lower()!=curTurtleColor):
        message_turtle.write(f"You Lose!😥\nThe {winning_color} turtle is the winner!", align="center", font=("Arial", 16, "normal"))
    else :
        message_turtle.write(f"You Won!🎉\nThe {winning_color} turtle is the winner!", align="center", font=("Arial", 16, "normal"))


screen = Screen()
screen.setup(width=500 , height=400)

colors = ['black','red' , 'orange' , 'yellow' , 'green' , 'blue']
y_positions = [-70 , -40 , -10 , 20 , 50 , 80]

all_turtles = []
user_bet = screen.textinput(title="PLay A Game !" , prompt="Which turtle will win the game:\n[black,red ,orange,yellow,green,blue]")

is_race_on = False

for turtle_index in range(0,6):
       new_Turtle = Turtle(shape='turtle')
       new_Turtle.color(colors[turtle_index])
       new_Turtle.penup()
       new_Turtle.goto(x=-230 , y=y_positions[turtle_index])
       all_turtles.append(new_Turtle)
 
 
if user_bet:
        is_race_on = True
 
while(is_race_on):
       for turtle in  all_turtles:
              if turtle.xcor()>230:
                     is_race_on = False
                     winning_color = turtle.pencolor()
                     display_message(user_bet , winning_color)
           
              random_distance = random.randint(0,10)
              turtle.forward(random_distance)
         
      
       
screen.exitonclick()



