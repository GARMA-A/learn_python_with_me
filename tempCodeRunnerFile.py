
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
          elif sum<=21 and sum >computerTwo