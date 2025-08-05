import random 
user= int(input("enter your choice (0 for rock, 1 for paper and 2 for Scissor): "))
if user>=3 or user<0 :
    print("invalid number . YOU LOSS")
else:
    computer= random.randint(0,2)
    print("computer choose:")
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






