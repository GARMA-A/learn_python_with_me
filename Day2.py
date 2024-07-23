def calcTips():
       print("welcome to the tip calculator" , end="\n")
       totalBill = float( input("What was the total bill ? $"))
       tip =  float(input("How mach tip percentage would you like to give 10 , 12 or 15 ? "))
       TipPlusBill = totalBill+((tip/100)*totalBill)
       numberOfPeoples = int(input("Enter the number of Peoble You want to split the bill with ? "))
       billForEach =  round( float(TipPlusBill/numberOfPeoples ),2)
       print("every one should give $",billForEach)

def calcRemainingTimeInYourLife():
       print("inter Your Age Now As integer ")
       myAgeNow = int(input())
       supposeDieAge = 65
       leftTimeInYears = supposeDieAge - myAgeNow
       leftTimeInWeeks = (leftTimeInYears*12)*4
       print(f"you will die after {leftTimeInWeeks} Weeks")

calcTips()
       



  
