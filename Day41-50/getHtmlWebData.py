import requests
import bs4



res = requests.get("https://github.com/GARMA-A/learn_python_with_me")


soup = bs4.BeautifulSoup(res.text)
print(soup.find(name='div' , class_="sr-only mt-n1"))








