#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list
# and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter
#  and assign their answer to a variable called guess. 
#  Make guess lowercase.

#TODO-3 - Check if the letter the user 
# guessed (guess) is one of the letters in the chosen_word.
#-------------------------------------------------------
#import random
#chosen_word = word_list[random.randint(0,2)]
#guess =input("guess a letter: ").lower()
# for letter in chosen_word:
#        if letter == guess:
#               print("Right")
#        else: print("Wrong")
#-------------------------------------------------------
#Step 2


#TODO-1:-Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display
#should be ["_", "_", "_", "_", "_"] 
#with 5 "_" representing each letter to guess.


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then
# reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was
# "apple", then display should be ["_", "p", "p", "_", "_"].


#TODO-3: - Print 'display' and you should see the guessed 
#letter in the correct position and every other letter 
# replace with "_".
#Hint - Don't worry about getting the user
# to guess the next letter. We'll tackle that in step 3.

#-----------------------------------------------------------
"""
chosen_word = word_list[random.randint(0,2)]

display = ['-'] * len(chosen_word) 

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

       for index in range(len(chosen_word)) :
        if chosen_word[index] == guess:
               oneFaildGuess==False
               display[index] = guess

       if oneFaildGuess == True:
            faildGuesses+=1

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
else : print("GAME OVER !")
     
 """      


#Step 2
#---------------------------------------------------------
#TODO add the stages when ever the user choice 
#wrong guess

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
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
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
import os


chosen_word = word_list[random.randint(0,2)]
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
else : print("GAME OVER !")  
               
         
       




