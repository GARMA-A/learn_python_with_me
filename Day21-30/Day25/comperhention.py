#--------------------
lst = [1,2,3]
new_list = [item*2 for item in lst ]
print(new_list)
#--------------------
rng = [x*2 for x in range(1,5)]
print(rng)
#--------------------
names = ['girgis' , 'garma' , 'memo' , 'koko' , 'lolo']

g_names = [name.upper() for name in names if name[0]=='g']
print(g_names)
#--------------------
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]

evens = [num for num in nums if num%2==0]
print(evens)
#--------------------
with open('num1.txt') as num1file:
       num1content = num1file.readlines()
       
with open('num2.txt') as num2file:
       num2content = num2file.readlines()
       
result = {num.strip() for num in num1content if num in num2content }
print(list(result))     

#--------------------  
import random
students_score = {name:random.randint(0,100) for name in names }
passed_students = {key:value for (key,value) in students_score.items() if value>=50 }
print(students_score)
print(passed_students)
#--------------------  
sentence = "today i will be a full stack we developer and i will be the king of the world"

my_dictionary = {key:len(key) for key in sentence.split(" ")}

print(my_dictionary)
#--------------------  
import csv
import pandas
with open("weather-data.csv") as csvfile:
       content = pandas.read_csv(csvfile)
       
       
# print(content)

#LOOP THROW THE ROWS in DATAFRAME

# for (index , row) in content.iterrows():
#        print(row.day) 
#        print("------------------")      

contentdict = {row.day:row.temp for index,row in content.iterrows()}
       
print(contentdict)



