# Give the number of Gray colors red and Black in the 
# big data file Primary Fur Color column

import pandas
import csv

my_dic = {
       "color":["grey","red","black"]
}

data_file = pandas.read_csv("big-Data.csv")

gray = len(data_file[data_file['Primary Fur Color']=="Gray"])
red = len(data_file[data_file['Primary Fur Color']=="Cinnamon"])
black = len(data_file[data_file['Primary Fur Color']=="Black"])

my_dic["count"] = [gray,red,black]

df = pandas.DataFrame(my_dic)

df.to_csv("myAnalysis.csv")



