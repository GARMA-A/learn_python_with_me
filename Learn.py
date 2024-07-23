#⚫⚫⚫⚫Day2⚫⚫⚫⚫
"""
Day2
******
🟥🟥🟥🟥🟥🟥 dataTypes
 len() give you the length ot the str
 type() give you the type of value you put in
 str() convert the value in () to str
 int() ~~~~~~~~~~~~~~~~~~~~~~ to int
 float() ~~~~~~~~~~~~~~~~~~~~~~ to float
 🟥🟥🟥🟥🟥🟥 math
 2**2  -> 2^2
 steps of mathimatical operations
 1.()
 2.**
 3.* or /
 4.+ or -
🟥🟥🟥🟥🟥🟥 math Functions
round(number , number_Of_Decimal_
Digits_To_End_With_After_Round)

roundNum = round(2.6666666,3)  output 2.667

floar division is return int instead of floar if you 
divide any two numbers

8//3   output 2 instead of 2.66666666665

🟥🟥🟥🟥🟥🟥 fString
f" you can here type number and text "
javaScript `your score is ${numberVariable} points` 
python f"your score is {numberVariable} points"

💹💹💹💹💹💹
Day2 END HERE!
"""
#⚫⚫⚫⚫Day4⚫⚫⚫⚫
"""
Day4
******
lists arrays

friends= ['girgis' , 'andrew' , 'kerolos' , 'shady' , 'poula']

you can use friends[1] -> andrew
and friends[-1] -> poula


friends.append("george") will edit the array and put george
as last element in the list 

you dont have 2D array build in python so you need to make it
like that :
list=[[t1,t2,t3],[t4,t5,t6],[t7,t8,t9],[t10,t11,t12]]
this is a 2D array  how ?!
if you want list[2][1] this will print t8 
the 3rd row 2nd column so for each row create a list
and each item in the list represent by colum number from
0 to 2
💹💹💹💹💹💹
Day4 END HERE!
"""

#⚫⚫⚫⚫Day5⚫⚫⚫⚫
"""
Day5
******* 
 for i in range(start number , last number , step increase or decrease )

  sum = 0
for i in range(1, 101 , 1): # to sum from 1 to 100 the 101 not count 
 sum = i+sum
 

print(sum)

random.Shufle() reorder the list randomly
random.choice(list)  select each time random element
from the list 
💹💹💹💹💹💹
Day5 END HERE!
"""

#⚫⚫⚫⚫Day7⚫⚫⚫⚫
"""
Day7
******
display = ['-'] * len(chosen_word)->hello
how to set default value and default size to a list 
['-' , '-' , '-' , '-' , '-'] 

💹💹💹💹💹💹
Day7 END HERE!
"""

#⚫⚫⚫⚫Day9⚫⚫⚫⚫
"""
Day9
******
dictionary in python

friends = {
  'first':{'hello' : ["h" , 'e' , 'l' , 'l' , 'o']},
  'second': {'right' : ['r' , 'i' , 'g' , 'h' ,'t']},
 'third': ['list' , 'with' , 'out' , ' obj']
}

friends = [
{'right' : ['r' , 'i' , 'g' , 'h' ,'t']}
{'hello' : ["h" , 'e' , 'l' , 'l' , 'o']}
]

array functions
🟥🟥🟥🟥🟥🟥 List (Array) functions
-----------------------------
my_list = [1, 2, 3, 4, 5]
-----
my_list[2] = 99  # Changes the third item (index 2) to 99
-----
my_list.remove(3)  # Removes the first occurrence 
of the value 3
-----
removed_item = my_list.pop(1)  
# Removes the item at index 1 and returns it
-----
del my_list[1]  # Deletes the item at index 1
-----
my_list.append(6)  # Adds 6 to the end of the list
-----
my_list.insert(2, 99)  # Inserts 99 at index 2
-----
my_list.extend([7, 8, 9])  # Adds 7, 8, 9 to the end of the list
you can do it also by that -> my_list+=[7,8,9] but 
you can not do that (my_list += 7  (ERROR))
-----

objects functions
🟥🟥🟥🟥🟥🟥 Dictionaries (objects) functions
-----------------------------
my_dict = {"name": "John", "age": 30, "city": "New York"}
-----
my_dict["age"] = 31  # Changes the value of "age" to 31
-----
removed_value = my_dict.pop("age") 
# Removes the item with key "age" and returns its value
-----
del my_dict["age"] 
# Deletes the item with key "age"
----
my_dict.clear()  
# Removes all items from the dictionary
-----
my_dict["country"] = "USA" 
# Adds a new key "country" with value "USA"

*************************************************
🟥🟥🟥🟥🟥🟥 Alter array of obj mutate 
the orignal array
*************************************************
# Original list of objects
original_list = [{'name': 'Alice'}, {'name': 'Bob'}]

# New object to be added
new_object = {'name': 'Charlie'}

# Add new object to the original list
original_list.append(new_object)

print("Modified original list:", original_list)
*************************************************
🟥🟥🟥🟥🟥🟥 Alter array of obj Not
mutate the orignal array
*************************************************
# Original list of objects
original_list = [{'name': 'Alice'}, {'name': 'Bob'}]

# New object to be added
new_object = {'name': 'Charlie'}

# Add new object to the original list
original_list.append(new_object)

print("Modified original list:", original_list)

💹💹💹💹💹💹
Day9 END HERE!
"""

#⚫⚫⚫⚫Day10⚫⚫⚫⚫
"""
Day10
******
there is title function that is convert 
the string to first lettr of each word to 
capital leterr and rest of the word to lower case
letters
for more information check Day 10 code
💹💹💹💹💹💹
Day10 END HERE!
"""

#⚫⚫⚫⚫Day17⚫⚫⚫⚫
"""
Day 17
******
OOP in python
class User:
  def __init__(self , userId , activity): # constractor
        self.userId = userId
        self.activity = "no_activity_yet"
        self.followers = 0
        self.folloeing = 0
  def followUser(self , user):
        user.followers+=1
        self.following+=1
        
the self is the current obj that you change to 
add attributes etc the OOP in python is 
very powerfull 
*************************************************
*************************************************
🟥🟥🟥🟥🟥🟥 LOOK To THIS Full EXAMPLE 
import os
class QuizBrain:
          
       def __init__(self,q_list):
              self.questionNumber = 0
              self.score = 0
              self.questionList = q_list
       def startQuiz(self):
              print(f"Q.{self.questionNumber+1} {self.questionList[self.questionNumber]['question']}")
              curAnswer = input("type 'True' or 'False' : ").lower()
              if(curAnswer==self.questionList[self.questionNumber]['answer']):
                     print("Right Answer")
              else:
                     print("Wrong Answer")
              self.questionNumber+=1
              self.calcScore(curAnswer==self.questionList[self.questionNumber]['answer'])
              input('press any key to continue...')
              os.system('cls')
              
       def calcScore(self,isCorrect):
              if(isCorrect):self.score+=1
              
       def endQuiz(self):
              print("Quiz has ended!😇")
              print(f"your score is {self.score}/12.")
*************************************************
*************************************************  
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain  

curQuiz = QuizBrain(question_data)  
 
for _ in range(11): 
       QuizBrain.startQuiz(curQuiz)
       
curQuiz.endQuiz()    
*************************************************
*************************************************       
      






💹💹💹💹💹💹
Day17END HERE!
"""

#⚫⚫⚫⚫nothing Day19⚫⚫⚫⚫
"""
Day 19
******
💹💹💹💹💹💹
Day19END HERE!
"""
#⚫⚫⚫⚫Day 20⚫⚫⚫⚫
"""
Day 20
****** snake game 
how to slice a list[] and typle()  python 
all that work on tupele also
('a','b','c')
piano_keys = ['a','b','c','d','e','f','g','h','i]

print (piano_keys[2:5]) will print ['c','d','e']
print (piano_keys[:5]) will print ['a','b','c','d','e']
print (piano_keys[2:]) will print ['c','d','e','f','g','h','i]

 
print (piano_keys[2:5:2])
the last :2 is to steps so that it will take one and  skip one 
will print  ['c','e']


print (piano_keys[::-1]) reverse the list for us 
will print ['i','h','g','f','e','d' , ....etc]















💹💹💹💹💹💹
Day20 END HERE!
"""
