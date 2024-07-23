#⚫⚫⚫⚫List⚫⚫⚫⚫
"""
list

all you need about list fast and has all info
https://www.geeksforgeeks.org/list-methods-python/

list.sorted() mutable => method update cur list
sorted(list) unmutable => function return new list

how to generate the index and the list with normal list
[(0,"first),(1,"second),(2,"third),(3,"fourth)]
https://www.geeksforgeeks.org/enumerate-in-python/

convert range(5) to [0,1,2,3,4] how range work
https://www.geeksforgeeks.org/python-range-method/

know the slicing convention in py(start , stop , step)
we rich the item before stop directily 
but not stop itself

list(range(20 , 2 , -1)) reverse printing  the list
or reversed(range(2,20,1)) 


how to do that [x**2 fro x in range(1,11)] =>
[1,4,9,16,25,36,49,64,81,100]
https://www.geeksforgeeks.org/python-list-comprehension/

slicing: print(nums[::]) will print [1,4,9,16,25,36,49]
https://www.geeksforgeeks.org/python-list-slicing/

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

       






