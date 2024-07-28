# file = open("test.txt") #open the file and store it as file data type 
# content = file.read()  # take all data in the file
# print(content)  # will print line by line in your file 
# file.close()
# you dont need to write close if you use this syntax

# with open("test.txt") as file:
       # content = file.read() # take all data from the file again
#but it will close outo if you out the with scope indent

# now we will take about W 'write'

# with open("test.txt") as file:
#        content = file.read() # take all data from the file again
# #but it will close auto if you out the with scope indent
# print(content) # this will give you an error because the file is not there yet

# by default the mode used is read 'r' and there is 'r+' for read and write
# and boss of them do not create new file automatically if it is not exists

# if you want to create a new file if it doesn't exist automatically
# you can use 'w' for just overwrite the file content or 'w+' for read and overwrite
# and both create new file if it doesn't exist

#if you just want to add some stuff to the end of the file and not overwrite it 
# you can use 'a' append or 'a+' for append and read


# with open("Day21-30/WorkWithFiles/test.txt" , 'w') as file:
#        file.write("hello\n")
#        file.write("welcome\n")
       
# with open("Day21-30/WorkWithFiles/test.txt" , 'a') as file:
#        file.write("add some stuff\n")
#        file.write("add some stuff\n")
#        file.write("add some stuff\n")
       
# with open("Day21-30/WorkWithFiles/test.txt" , 'r') as file:
#        content = file.read()
#        print(content) 



# Work with json data is a bit different just diffrent in two lines 


# import json

# file_name = 'data.json'
# with open(file_name, 'r') as file:
#     data = json.load(file)   #<== that  line work like read excatly

# new_entry = {"name": "Charlie", "age": 35}
# data.append(new_entry)
# #data.clear() #clear all json entries

# with open(file_name, 'w') as file:
#     json.dump(data, file, indent=4)  #<== that  line work like write excatly
                                       # if it 'w' will overwrite or 'a' append

# print(f"New entry added to {file_name}.")


# fetch Json from API and Put the data in local file


# import requests
# import json

# url = 'https://dummyjson.com/users'

# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()  # Parse the JSON response   
#     with open("data.json",'w') as myJsonFile:
#       json.dump(data, myJsonFile , indent=4) # put the fetched data into file
      
#     with open("data.json",'r') as myJSON:
#         content = json.load(myJSON)   # take the data from the file
#         print(content)
     
# else:
#     print(f"Failed to fetch data. Status code: {response.status_code}")


       



