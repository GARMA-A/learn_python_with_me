alphabet = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q','r', 's', 't', 'u', 'v', 'w', 'x',
'y','z'
]
def Encrypt(key , plain):
       Cipher =""
       for ch in plain:
          if(ch==" "): 
            Cipher+=" "
          else :
            Cipher += alphabet[(alphabet.index(ch) + int(key))%26]
       return Cipher
def Decrypt(key , cipher):
     plain=""
     for ch in cipher:
          if(ch==" "): 
              plain+=" "
          else :
              plain += alphabet[(alphabet.index(ch) - int(key))%26]
     return plain

continueLooping = True
while(continueLooping):
 choice = input("Type 'encode' to encrypt type 'decode' to decrept : ")
 if(choice== 'encode'):
      plain=input("Type your message to encrypt : ")
      key = int(input("Type number of Shifts : "))
      print(Encrypt(key , plain.lower()))
 elif (choice=='decode'):
      cipher=input("Type your message to decrypt : ")
      key = int(input("Type number of Shifts : "))
      print(Decrypt(key , cipher.lower()))
 if(input('Type "yes" to contuniue and "no" for Stop : ')=="no"):
      continueLooping = False
 



# import math    
# def isPrime(num):
#      if(int(num)<=2):return False
#      else : 
#       for i in range(2 , math.ceil( math.sqrt(int(num))+1) ):
#           if(int(num)%i==0): return False
#      return True

# num = input("Enter a number : ")
# if(isPrime(num)):
#     print("Prime Number!")
# else : print("Not Prime NUmber")
          
     



