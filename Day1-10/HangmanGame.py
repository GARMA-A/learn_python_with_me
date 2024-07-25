import random
import os
word_list = [
    "apple", "banana", "carrot", "elephant", "giraffe",
    "hamster", "jacket", "kangaroo", "lemon", "mango",
    "nutmeg", "orange", "peanut", "quinoa", "rabbit",
    "strawberry", "tomato", "umbrella", "violet", "watermelon",
    "xylophone", "yogurt", "zebra", "antler", "ballerina",
    "cabbage", "dolphin", "eggplant", "firefly", "garden",
    "honey", "insect", "jackal", "kettle", "leopard",
    "marmot", "nectar", "ostrich", "penguin", "quail",
    "raccoon", "sunflower", "tulip", "unicorn", "violet",
    "waterfall", "xylophone", "yogurt", "zeppelin"
]

stages = [
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
,

'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''
, 

'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''
,

 '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''
,

 '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',

 '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print("-------------------------------")
print("\n")
print("\n")
tryAgain = True

while tryAgain:
 os.system('cls')

 chosen_word = word_list[random.randint(0,49)]
 display = ['-'] * len(chosen_word) 

 stageIndex = len(stages)

 print('[ ' ,end="")
 for item in  display :
       print("' "+item+" '"+" " , end="")
 print('] ')

 inProgress = True
 faildGuesses = 0




 while(inProgress):
       isTheWordComplete = True
       oneFaildGuess = True
       guess =input("guess a letter: ").lower()
       os.system('cls')
      
       print("-------------------------------")
       print("\n")
       print("\n")
       for index in range(len(chosen_word)) :
          if chosen_word[index] == guess:
               oneFaildGuess=False
               display[index] = guess

       if oneFaildGuess == True:
            faildGuesses+=1
            stageIndex-=1

       if(not(stageIndex==len(stages))):
            print(stages[stageIndex])

       print('[ ' ,end="")

       for item in  display :
         if(item=='-'):
              isTheWordComplete= False
         print("' "+item+" '"+" " , end="")


       print('] ' ,end="\n")

       if(faildGuesses>=7 or isTheWordComplete ):
            inProgress= False
      
    

 if(isTheWordComplete):
      print("You Save The Man🎉")
 else : 
  print("The man died!💀")
  print(f"The word was '{chosen_word}'\n ")  
  tryAgain = input("play Again ! type 'yes' or 'no' :").lower()=='yes'
  
               
         
       




