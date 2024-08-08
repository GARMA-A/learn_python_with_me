import bs4
import requests


# res = requests.get("https://www.python.org/")

# soup = bs4.BeautifulSoup(res.text)
# list = [el.get_text() for el in soup.select(".shrubbery ul li") ]
# list =  list[5:10]

res = requests.get("https://raw.githubusercontent.com/GARMA-A/QuizData/main/phases.json?token=GHSAT0AAAAAACVKPFZRWUSILLNNCM5AVQOGZVUBNUQ")
print(res.json())








