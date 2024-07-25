def tresureIslandGame():
       print("Welcome to Tresure Island. ",end='\n')
       print("Your Mission is To Find The Treasure. ",end='\n')
       input("To Start Enter Any KEY...")
       print("You're at a cross road. where do you want to go ?" , end='\n')
       print("1.left         2.right" , end='\n')
       directionToGo = str(input())
       if directionToGo =="left":
              print("You come to a lake . There is  an Island in the middle of the lake.",end='\n')
              print("Type \"wait\" to wait for a boat. type \"swim\" to swim across ",end='\n')
              waitOrSwim = str(input())
              if waitOrSwim=='wait':
                     print("You arrive at the iland unharmed. There Is house with 3 doors. One red , one Yellow and one Blue" , end='\n')
                     print("which color do you choose ?" , end='\n')
                     color = str(input())
                     if color == 'red':
                            print("its aroom full of fire Game Over")
      







