#normal way of taking data from file

# with open("weather-data.csv") as data_file:
#       content_list = data_file.readlines()
      
# print(content_list)       

# special way for the .csv files 


# import csv

# with open("weather-data.csv") as data_file:
#       content_list = csv.reader(data_file)
#       for row in content_list:
#              print(row)
      
#Data analysis with pandas


import pandas

weather_file = pandas.read_csv("weather-data.csv")
print(weather_file)
print(weather_file.temp)

#Data Frame is a table 
#series is the column
#and a seires with condition is a row

#Working with Series
print(weather_file.temp.to_list())
print(weather_file.temp.to_dict())
print(weather_file.temp.mean())
print(weather_file.temp)

#Working with Rows

print(weather_file[weather_file.temp==weather_file.temp.max()])
print(weather_file[weather_file.day=="Monday"])


#Creating DataFrame

data_dict = {
       "students" :['ali','koko','lolo'],
       "scores": [76,56,65] 
}
data_frame  = pandas.DataFrame(data_dict)
print(data_frame)

