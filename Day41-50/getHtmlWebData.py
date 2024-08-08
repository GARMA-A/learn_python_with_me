import requests
import bs4



res = requests.get("https://www.empireonline.com/movies/features/best-movies-2")


soup = bs4.BeautifulSoup(res.text , features="html.parser")
my_list = [h3.get_text() for h3 in soup.find_all(name='h3' , class_="listicleItem_listicle-item__title__BfenH")]
my_list = my_list[::-1]
print(my_list)

with open("movies.txt",'w') as my_file:
       for movie in my_list:
        my_file.write(movie+'\n')
        







