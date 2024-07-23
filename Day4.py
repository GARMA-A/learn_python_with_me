import random

def selectRandomName():
      
       while(True):
        x = bool( input("type True of False : ") )
        friends = ['girgis' , 'andrew' , 'kerolos' , 'shady' , 'poula' ,'george']
        randomIndex = random.randint(0,5)
        print(f"the one who must pay the dinner is {friends[randomIndex]}")
        if(x==False): break

       
selectRandomName()