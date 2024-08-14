# Welcome to The complete Python Reference

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQX9_SPWYSde7MuHUlFOXhKy7GEjn-Ta1W3iyVT_YDWKfiuO7IcaTb8BSDnlCG6HUN0bN4&usqp=CAU" width="300" height="450" />


#### For more in-depth learning and reference, check out the book [here](https://drive.google.com/file/d/1PQM8tYsdCcAAaiBmx83EYnhbYyLvetF9/view).

## **Python Summary (the Basics)**

```Python
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

```

```python
#⚫⚫⚫⚫List⚫⚫⚫⚫
"""
list

all you need about list fast and has all info
https://www.geeksforgeeks.org/list-methods-python/


how to generate the index and the list with normal list
[(0,"first),(1,"second),(2,"third),(3,"fourth)]
https://www.geeksforgeeks.org/enumerate-in-python/

convert range(5) to [0,1,2,3,4] how range work print(list(range(5)))
https://www.geeksforgeeks.org/python-range-method/

know the slicing convention in py(start , stop , step)
we rich the item before stop directily 
but not stop itself

list(range(20 , 2 , -1)) reverse printing  the list
or reversed(range(2,20,1)) 


how to do that [x**2 for x in range(1,11)] =>
[1,4,9,16,25,36,49,64,81,100]
https://www.geeksforgeeks.org/python-list-comprehension/

slicing: print(nums[::]) will print [1,4,9,16,25,36,49]
https://www.geeksforgeeks.org/python-list-slicing/

LISTS FROM THE BOOK
'''
apend(val) => add to the end 

index(val)=>return index of first accourence or error valueErorr

insert(index,val) =>if that index already have el will push it to front

del listName[index] =>del this el from the list
pop(index) =>delete last el or at index (optional) 

use help(listName.method) for how to use 


list.sorted() => method update cur list
sorted(list) => method update cur list

listName.reverse()=> method update cur list
reversed(listName) =>method update cur list





'''

"""
#⚫⚫⚫⚫Dictionaries⚫⚫⚫⚫
"""
random_things= [
  {'name': 'statistics',
  'type': 'list',
  'content':[12.2,45.99,64.78]
  },
 {'name': 'math',
  'type': 'list',
  'content':[1,2,3,4]
  },
 {'name': 'monsters',
  'type': 'list',
  'content':["bob","simon","kiloa"] 
  }
 ]
 
 you can del random_things[0][content]
 
 
random_things[0]['address'] will throw ERROR
but random_things[0].get('address') will just print none

loop trow it
for obj in random_things:
    for key,value in obj.items():
        print("key:",key,"value:",value)
    print("--------------------------------")


"""
#⚫⚫⚫⚫Tuple⚫⚫⚫⚫
"""
Tuples
(1,2,3) like list but you cannot change its values after
initialization
https://www.geeksforgeeks.org/python-tuples/

"""
#⚫⚫⚫⚫Sets⚫⚫⚫⚫
"""
sets in python
https://www.geeksforgeeks.org/set-theory/

sets like the sets you take in the probability


"""
#⚫⚫⚫⚫Functions⚫⚫⚫⚫
'''
functions in python

#print(f"{124.23456:.2f}") => 124,23
# Clean Functions 
# def add(s1:int , n2:int)->int:
#  """this is a function for adding 
#  two numbers only"""
#  return s1 + n2

# help(add) this will show the args and  doc string without 
# need to go to the function if it in another file 

# arbitrary arguments lists
def average(*args):
       return sum(args)/len(args)

# sum = 10 + 15 
# print(sum)
# print(type(sum))
# print(sum([10 , 1]))

# python automatic pass by reference to function
id() =>return the memory address

# x = 10

# def f(x):
#       print(id(x))  #pass by reference
#       x=x*10
#       print(id(x))  #create new variable to srore the changes  
#       return x

# print(id(x))
# print(f(x))
# print(x)

There is map Filter Reduce like javascript 100%

def cuber(x):
 return x**3

my_list =list(map(cuber,[1,2,3]))
print(my_list)



def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))




from functools import reduce  #### import first ####

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)
print(total)

anonymous functions 
# lambda <argument> : expersion
f = lambda a:a+10

usualy it used by map filter reduce  sorting 
print(list(map(lambda a:a+10,[1, 2, 3, 4, 5])))

the_champions = [
       "girgis emad" , "ramy xlia" ,
       "ahmed ali" , "mosad kariem"
       ]

the_champions.sort(key=lambda name:name.split(' ')[-1])
print(the_champions)

def build_profile(first , second , **user_info):
    user_info['first_name'] = first
    user_info['second_name'] = second
    return user_info
print(build_profile("girgis" , "emad" ,first_phone="12345764",second_phone="973483203"))
output => {'first_phone':"12345764", 'second_phone':"973483203",'first_name':"girgis", 'second_name':"emad"}
    
'''
#⚫⚫⚫⚫Classes⚫⚫⚫⚫
'''
Dunder Methods are some method you  can add to your class
to give to it some functionality like set item  get item take the len
of the cur item in the cur obj of the class and more...

class MyCollection:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __iter__(self):
        return iter(self.items)

    def __str__(self):
        return f"MyCollection with items: {self.items}"

# Example usage
collection = MyCollection([1, 2, 3])
print(len(collection))     # Output: 3
print(collection[1])       # Output: 2
collection[1] = 42
print(collection[1])       # Output: 42
del collection[1]
print(list(collection))    # Output: [1, 3]
print(collection)          # Output: MyCollection with items: [1, 3]
----------------------------------------------------------------
----------------------------------------------------------------
----------------------------------------------------------------
----------------------------------------------------------------
----------------------------------------------------------------
----------------------------------------------------------------
----------------------------------------------------------------
use help(Dog) to see all info

class Dog:
    """This is a simple docstring
    to know how this class should be used"""
    
    def __init__(self, name="bob", age="0"):
        self.name = name
        self.age = age

    @property  # the getter in python
    def name(self):
        return self._name  # _ is optional

    @name.setter  # the setter in python
    def name(self, name):
        if not name.isalpha():
            raise ValueError("Invalid name")
        self._name = name

    @property  # the getter in python
    def age(self):
        return self._age  # _ is optional

    @age.setter  # the setter in python
    def age(self, age):
        if not age.isdigit():
            raise ValueError("Invalid age")
        self._age = age
       
'''
#⚫⚫⚫⚫Imports⚫⚫⚫⚫
"""
import fileName 
now you can access all functions and classes in this file(module)

from fileName import class or method
now you can use this class or method in this file(module) only





"""
#⚫⚫⚫⚫base libs⚫⚫⚫⚫
"""
you need to know about the standard library 
study them hard 

random
math 
statistics
deciaml
array 
collections
string
sys
os
shutil
glob
re  =>regular expression
datetime
time
json
csv 

"""
#⚫⚫⚫⚫Files⚫⚫⚫⚫
"""
Output file:
with open('pi_digits.txt') as file_object:
    content = file_object.read()
print(content.strip())

line by line:
with open('pi_digits.txt') as file_object:
    for line in file_object:
       print(line.strip())
       
list of lines:       
file_name = "pi_digits.txt"
with open(file_name) as file_object:
     content = file_object.readlines()
     
print(type(content))
print(content)


just be writable and remove the past writing:
with open(file_name,'w') as myfile:
    myfile.write("this will write into the file and remove any thing else")
    
with open(file_name,'w+') as myfile:
    myfile.write("this will write into the file and remove any thing else")
    myfile.write("will apear just this two lines in the file")
    
    
how to not remove past content but just add to it (apend):
with open(file_name,'a') as myfile:
    myfile.write("this will just add to the end of main file content")
    myfile.write("this also just add to the main end of file content")

'w' (write)
Opens the file for writing.
Creates a new file if it does not exist.
Truncates the file to zero length if it exists, meaning any existing content is deleted.
You can only write to the file; you cannot read from it.

'w+' (write and read)
Opens the file for both writing and reading.
Creates a new file if it does not exist.
Truncates the file to zero length if it exists, meaning any existing content is deleted.
Allows both reading and writing to the file.

'r+' (read and write)
Opens the file for both reading and writing.
The file must already exist. If the file does not exist, an error will occur.
Does not truncate the file, so the existing content is preserved.
Allows both reading and writing to the file, with the file pointer positioned at the beginning.


'a' (append)
Opens the file for writing.
Creates a new file if it does not exist.
If the file exists, the file pointer is positioned at the end of the file. The new data will be written at the end of the file, preserving existing content.
You can only write to the file; you cannot read from it.

'+a' (append and read)
Opens the file for both appending and reading.
Creates a new file if it does not exist.
If the file exists, the file pointer is positioned at the end of the file for writing, meaning any new data will be written at the end of the file.


check if the file exists before do an operation if you dont want 
to create a new file automatically instead maybe you need to
rise error if file does not exist

import os

file_name = 'example.txt'

if os.path.exists(file_name):
    with open(file_name, 'a') as myfile:
        myfile.write('Appending this text to the file.\n')
else:
    raise FileNotFoundError(f"The file {file_name} does not exist.")
    
    
    
Read JSON file And Add one obj to it 
also Can Clear it and write new data

import json

file_name = 'data.json'
with open(file_name, 'r') as file:
    data = json.load(file)

new_entry = {"name": "Charlie", "age": 35}
data.append(new_entry)
#data.clear() #clear all json entries

with open(file_name, 'w') as file:
    json.dump(data, file, indent=4)

print(f"New entry added to {file_name}.")


fetch Json from API and Put the data in local file


import requests
import json

url = 'https://dummyjson.com/users'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()  # Parse the JSON response   
    with open("data.json",'w') as myJsonFile:
      json.dump(data, myJsonFile , indent=4) # put the fetched data into file
      
    with open("data.json",'r') as myJSON:
        content = json.load(myJSON)   # take the data from the file
        print(content)
     
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")


"""
#⚫⚫⚫⚫Exceptions⚫⚫⚫⚫
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("you cannot divide by zero")
    
using the else block:

num1 = int(input("enter a number :"))
num2 = int(input("enter a number :"))
try:
    result = num1 / num2
except ZeroDivisionError:
    print("you cannot divide by zero")
else:
    print(result)
    
you  can just use rise to rise your own excepcion
    
    def check_value(value):
    if value < 0:
        raise ValueError("Value must be non-negative")
    return value

try:
    check_value(-1)
except ValueError as e:
    print(e)
    
    
    
try:
    # Code that might raise an exception
    raise ValueError("Invalid value")
except ValueError as e:
    # Code that runs if an exception occurs
    print(e)# e is the message that was raised
    
    
    


"""

# python -m pip uninstall colorgram.py



seg = [1,2,3,4,5,6]

for i in range(5,-1,-1):  # 0 , 1 ,  2 , 3 , 4 , 5 
    print(seg[i])



```


