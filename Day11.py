import random
import os


card_numbers = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
max_number = 21
computerTwoCards = [random.choice(card_numbers),random.choice(card_numbers)]



playAgain = True  
myCards = [random.choice(card_numbers),random.choice(card_numbers)]
if input("Do you want To Play a Game BlackJack ? type 'y' or 'n' : ") == 'y':
   while(playAgain):
      os.system('cls')
      print(f"Computer first card is {computerTwoCards[0]}")
      print("Your cards now is : [ "  ,end="")
      for cardNumber in myCards:
         print(f"{cardNumber} " , end="")
      print(']')
      if input("Do you want to add a Card ? type 'y' or 'n' : ") =='y':
        myCards.append(random.choice(card_numbers)) 
      else :
          os.system('cls')
          print(f"computer cards are [{computerTwoCards[0]} and {computerTwoCards[1]}]")
          print("Your cards now is : [ " , end="")
          sum = 0
          for cardNumber in myCards:
             sum+=cardNumber
             print(f"{cardNumber} " , end="")
          print(']')
          if sum>21 or sum<computerTwoCards[0]+computerTwoCards[1]:
             print("You Lose!💔")
             playAgain = False
          elif sum<=21 and sum >computerTwoCards[0]+computerTwoCards[1]:
             print("You Won🥳")
             playAgain = False
          else : 
             print("Draw !🏳️")
             playAgain = False

else : print("Thanks for join us ")

print("The Game Over")





