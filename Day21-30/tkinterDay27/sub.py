#make a tuple of args
def add (*args):
       print(sum(args))
       
       
add(1,2,3,4,5,6)

#make dictionary of args

def calculator(**kwargs):
       add_number1 =kwargs.get('add1')
       add_number2 =kwargs.get('add2')
       if(add_number1 != None and add_number2 != None):
        print(add_number1+ add_number2)
       
       
       

calculator(add1=3 , multiply = 5)