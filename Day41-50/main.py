from bs4 import BeautifulSoup

with open("website.html" ,encoding='utf-8') as html_file:
       content = html_file.read()
       
soup = BeautifulSoup(content,"html.parser")
# print(soup.title)
# print(soup.h1)
all_a_tags = soup.find_all(name="a")
print(all_a_tags) #list of all a in html file

for tag in all_a_tags:
       print(tag.get("href"))# anly the https:// part
       
# give me the first h1 you face with id = "name"
heading =soup.find(name='h1',id="name") 
print(heading)
# give me the first h1 you face with class = "name"
heading2 =soup.find(name='h3',class_="heading") 


# give me the first a inside p you face 
company_url = soup.select_one(selector="p a")
print(company_url)

# give me the first element with id = "name"
name = soup.select_one(selector="#name")

# select all elements that have a class of heading
all_headings = soup.select(".heading")
print(name)



# see the documnetation for how to take data from html files
   
   

