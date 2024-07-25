import os

def askAndReturnDolars():
       quarterNumber = float( input("\nEnter quarter(25cent) coins number : ") or 0) 
       dimeNumber = float(input("\nEnter Dime(10cent) coins number : ") or 0) 
       nickelNumber = float(input("\nEnter nickel(5cent) coins number : ") or 0) 
       pennyNumber = float(input("\nEnter penny(1cent) coins number : ") or 0) 
       
       DolarsAmount= round(float((quarterNumber*25 + dimeNumber*10 + nickelNumber*5 + pennyNumber)/100),2)

       return DolarsAmount
       
coffeMachineAscii = """
     _________
    |         |
    |  _____  |
    | |     | |
    | |     | |
    | |_____| |
    |_________|
    |    |    |
    |    |    |
    |____|____|
"""

# water in ml coffee in gram milk in ml   (ml->Milli Liter)
machineResourses = {'water':300 , 'milk':200 , 'coffee' :100 , "money":round(float(0.00),2), 'curPayOperation': round(float(0.00),2)}

espressoRequirements ={'water':50 , 'coffee':18 , 'money':1.5 }

latteRequirements ={'water':200 , 'coffee':24 ,'milk':150 , 'money':2.5 }

capucionRequirements ={'water':250 , 'coffee':24 , 'milk':100 , 'money':3.0 }

Exit = False

while not Exit :
 os.system('cls')
 

 complete = False
 print(coffeMachineAscii)

 coffeeType = input("\nPLease Enter the coffee type you want. \n type 'espresso' , 'latte' or 'capucino' : ").lower() or 'nop!'

 if coffeeType == 'nop!' :
     Exit =input("\nYou must Enter a Type ! type 'y' to contuniue or 'n' to Exit  : ").lower() =='n'

 elif coffeeType=='report' :
     print(f"\nWater : {machineResourses['water']}ml")
     print(f"\ncoffee : {machineResourses['coffee']}gram")
     print(f"\nmilk : {machineResourses['milk']}ml")
     print(f"\nmoney : {machineResourses['money']}$")

     Exit = input("\nDo You Want To Exit The Programm ? type 'y' or 'n' : ").lower()=='y'

 elif coffeeType == 'espresso'\
 and machineResourses['coffee']>=espressoRequirements['coffee']\
 and machineResourses['water']>=espressoRequirements['water'] : 
    complete= input("\nespresso Price is 1.5$ do you want to contuniue ? type 'y' or 'n'  : ").lower()=='n'

    while not complete :

       moneyInDollars = askAndReturnDolars()
       machineResourses['curPayOperation'] += moneyInDollars

       if espressoRequirements['money'] - machineResourses['curPayOperation']== 0  :
              print("\nDone ! your coffee will be ready in a minute...")

              machineResourses['money']+=machineResourses['curPayOperation']
              machineResourses['water']-=espressoRequirements['water']
              machineResourses['coffee'] -= espressoRequirements['coffee']
       
              Exit = input("\nDo You Want To Exit The Programm ? type 'y' or 'n' : ").lower()=='y'

              machineResourses['curPayOperation'] = 0

              complete = True


       elif espressoRequirements['money'] - machineResourses['curPayOperation'] > 0:

              complete=input(f"\nyou still need to pay {round( float(espressoRequirements['money'] -  machineResourses['curPayOperation']) , 2)}\
              to complete  'complete' , 'dont complete' : ")!='complete'



       elif espressoRequirements['money'] -  machineResourses['curPayOperation'] < 0 :
              complete = True

              print(f"\nDone ! you will receive rest of your money { round( machineResourses['curPayOperation']-espressoRequirements['money'],2)}$.\n\
                  your coffee will be ready in a minute... ")
              machineResourses['water']-=espressoRequirements['water']
              machineResourses['coffee'] -= espressoRequirements['coffee']
              machineResourses['money']-= round( machineResourses['curPayOperation']-espressoRequirements['money'],2)

              machineResourses['money']+=machineResourses['curPayOperation']

              machineResourses['curPayOperation'] = 0
              
              Exit = input("\nDo You Want To Exit The Programm ? type 'y' or 'n' : ").lower()=='y'

          
            


 elif coffeeType == 'espresso'\
  and machineResourses['coffee']<espressoRequirements['coffee']\
  or machineResourses['water']<espressoRequirements['water']  :
  
  print("\nNot enough resourses in the machine try again soon !")
  Exit = input("\nDo You Want To Exit The Programm ? type 'y' or 'n' : ").lower()=='y'







 elif coffeeType == 'latte'\
  and machineResourses['milk']>=latteRequirements['milk'] and machineResourses['coffee']>= latteRequirements['coffee']\
  and machineResourses['water']>=latteRequirements['water']:
      complete= input("\nlatte Price is 2.5$ do you want to contuniue ? type 'y' or 'n'  : ").lower()=='n'

      while not complete :
          
          moneyInDollars = askAndReturnDolars()
          machineResourses['curPayOperation'] += moneyInDollars

          if latteRequirements['money'] - machineResourses['curPayOperation']== 0  :
              print("\nDone ! your coffee will be ready in a minute...")

              machineResourses['money']+=machineResourses['curPayOperation']
              machineResourses['water']-=latteRequirements['water']
              machineResourses['coffee'] -= latteRequirements['coffee']
              machineResourses['milk'] -= latteRequirements['milk']
       
              Exit = input("\nDo You Want To Exit The Programm ? type 'y' or 'n' : ").lower()=='y'

              machineResourses['curPayOperation'] = 0

              complete = True


          elif latteRequirements['money'] - machineResourses['curPayOperation'] > 0:

              complete=input(f"\nyou still need to pay {round( float(latteRequirements['money'] -  machineResourses['curPayOperation']) , 2)}\
              to complete  'complete' , 'dont complete' : ").lower()!='complete'



          elif latteRequirements['money'] -  machineResourses['curPayOperation'] < 0 :
              complete = True

              print(f"\nDone ! you will receive rest of your money { round( machineResourses['curPayOperation']-latteRequirements['money'],2)}$.\n\
                  your coffee will be ready in a minute... ")
              
              machineResourses['water']-=latteRequirements['water']
              machineResourses['coffee'] -= latteRequirements['coffee']
              machineResourses['milk'] -= latteRequirements['milk']
              machineResourses['money']-= round( machineResourses['curPayOperation']-latteRequirements['money'],2)
              machineResourses['money']+=machineResourses['curPayOperation']
              machineResourses['curPayOperation'] = 0
              
              Exit = input("\nDo You Want To Exit The Programm ? type 'y' or 'n' : ").lower()=='y'

          
          
     



     

 elif coffeeType == 'latte'\
  and machineResourses['milk']<latteRequirements['milk'] or machineResourses['coffee']< latteRequirements['coffee']\
  or machineResourses['water']<latteRequirements['water']:   

   print("\nNot enough resourses in the machine try again soon !")
   Exit = input("\nDo You Want To Exit The Programm ? type 'y' or 'n' : ").lower()=='y'
  







 elif coffeeType == 'capucino'\
  and machineResourses['milk']>=capucionRequirements['milk'] and machineResourses['coffee']>= capucionRequirements['coffee']\
  and machineResourses['water']>=capucionRequirements['water']:
      complete= input("\nlatte Price is 3.0$ do you want to contuniue ? type 'y' or 'n'  : ").lower()=='n'

      while not complete :
          
          moneyInDollars = askAndReturnDolars()
          machineResourses['curPayOperation'] += moneyInDollars

          if capucionRequirements['money'] - machineResourses['curPayOperation']== 0  :
              print("Done ! your coffee will be ready in a minute...")

              machineResourses['money']+=machineResourses['curPayOperation']
              machineResourses['water']-=capucionRequirements['water']
              machineResourses['coffee'] -= capucionRequirements['coffee']
              machineResourses['milk'] -= capucionRequirements['milk']
       
              Exit = input("Do You Want To Exit The Programm ? type 'y' or 'n' : ").lower()=='y'

              machineResourses['curPayOperation'] = 0

              complete = True


          elif capucionRequirements['money'] - machineResourses['curPayOperation'] > 0:

              complete=input(f"you still need to pay {round( float(capucionRequirements['money'] -  machineResourses['curPayOperation']) , 2)}\
              to complete  'complete' , 'dont complete' : ").lower()!='complete'



          elif capucionRequirements['money'] -  machineResourses['curPayOperation'] < 0 :
              complete = True

              print(f"Done ! you will receive rest of your money { round( machineResourses['curPayOperation']-capucionRequirements['money'],2)}$.\n\
                  your coffee will be ready in a minute... ")
              
              machineResourses['water']-=capucionRequirements['water']
              machineResourses['coffee'] -= capucionRequirements['coffee']
              machineResourses['milk'] -= capucionRequirements['milk']
              machineResourses['money']-= round( machineResourses['curPayOperation']-capucionRequirements['money'],2)
              machineResourses['money']+=machineResourses['curPayOperation']
              machineResourses['curPayOperation'] = 0
              
              Exit = input("Do You Want To Exit The Programm ? type 'y' or 'n' : ").lower()=='y'

          
          
     



     

 elif coffeeType == 'capucino'\
  and machineResourses['milk']<capucionRequirements['milk'] or machineResourses['coffee']< capucionRequirements['coffee']\
  or machineResourses['water']<capucionRequirements['water']:   

   print("Not enough resourses in the machine try again soon !")
   Exit = input("Do You Want To Exit The Programm ? type 'y' or 'n' : ").lower()=='y'


 else :
      print("You Write Somthing inCorrect please Try Agin")
      Exit = input("Type 'y' for try again or 'n' for Exit").lower()=='n'
      
