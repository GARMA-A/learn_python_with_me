

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

audience = []
thereIsMore = True
print(logo)
print("Welcome to the secret auction program")
while(thereIsMore):
  name = input("What is your name : ")
  price = int( input("what is the price you will spend : $"))
  newObj = {'name':name , 'price':price}
  audience.append(newObj)
  if(input("There is More ? type 'yes' or 'no' ")=='no'):
    thereIsMore = False

winner = {}
curMxPrice = 0
for person in audience:
  if(person['price']>curMxPrice):
    curMxPrice=person['price']
    winner['name'] = person['name']
    winner['price'] = person['price']

print(f"The winner name is {winner['name']}")
print(f"with price of {winner['price']}")

  
  


