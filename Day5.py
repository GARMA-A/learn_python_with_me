import random

def randomPassword():
  password=[]
  randomPass = ""
  print("how many letters would you like in your Password ?")
  numberOfLetters = int(input())
  for _ in range(numberOfLetters):
    randomLetter = chr(random.randint(97 ,122))
    password +=randomLetter
  print("how many sympols would you like ?")
  numberOfSympols = int(input())
  for _ in range(numberOfSympols):
    randomSympol = chr(random.randint(33,38))
    password += randomSympol
  print("how many numbers would you like ?")
  numberOfNumbers = int(input())
  for _ in range(numberOfNumbers):
    randomNumber = random.randint(0,9)
    password += str(randomNumber)
  random.shuffle(password)
  for ch in password:
    randomPass+=ch
  print(randomPass)
    
  
randomPassword()



    
