import random 
rock='''
rock      /---]
--------[_____]
--------[_____]
--------[_____]
--------[_____]
        \____]
'''
paper= '''
paper   /_|_|]
--------[__|___|__]
--------[__|___|__]
--------[__|___|__]
--------[__|___|__]
        [_|__|__]
'''

scissors='''
scissors /]
--------/__|__|__)
--------)
--------\___|__|__)
--------[___]
--------\__]
        
'''
game_image=[rock,paper,scissors]
user= int(input("enter your choice (0 for rock, 1 for paper and 2 for Scissor): "))
if user>=3 or user<0 :
    print("invalid number . YOU LOSS")
else:
    print(game_image[user])
    computer= random.randint(0,2)
    print("computer choose:")
    print(game_image[computer])
    print(computer)

    if computer==user :
         print("Its a draw")

    elif computer==2 and user ==0:
        print("YOU WINSS")

    elif computer==0 and user ==2:
        print("YOU LOSS")


    elif computer>user :
        print("YOU LOSS")

    elif computer<user :
        print("YOU WINSS")






