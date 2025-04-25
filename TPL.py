#TPL (TAMBE PREMIERE LEAGUE)
import sys
import random
import string
score=0 #user score
score1=0 #opponent score
count=0
a=input("What would you like to do? play or exit:")
print("NOTE: You can play this game 6 times only,so play carefully, Enjoy!")
print("------------------------------------")
if a=="play" or a=="PLAY" or a=="Play":
    while count<6:
        count+=1
        try:
            user=int(input("Enter the number between 1-6:"))
            opponent=random.choice([1,2,3,4,5,6])
            print("Opponent input between 1-6 is:",opponent) #opponent just to say another player
            if 0<user<=6 and 0<opponent<=6:
                if user==opponent:
                    print("You are out")
                    print("-----------------------------")
                    print("user score is:",score)
                    print("-------------------------------")
                    print("opponent score is:",score1)
                    break
                elif user<opponent:
                    print("opponent won")
                    score1+=opponent
                    score+=user
                    print("Opponent score is:",score1)
                    print("user score is:",score)
                    print()
                elif user>opponent:
                    print("user won")
                    score+=user
                    score1+=opponent
                    print("user score is:",score)
                    print("Opponent score is:",score1)
                    print()
            else:
                print("Inputs are suppose to be between 1-6")
        except ValueError:
            print("Strings values are not expected,You should enter an integer")
    print("------------- Score Evaluation----------------")
    print("The final score of user is:",score)
    print("The final score of opponent is:",score1)
    print()
    print("-----------------Final Result--------------------")
    if score>score1:
        print("User has won the game:",score)
    elif score1>score:
        print("opponent has won the game:",score1)
elif a=="exit" or a=="EXIT" or a=="Exit":
        print("Exit is done successfully")
        sys.exit()
else:
    print("Expected input is play or exit, no other input is expected")
    print("---------------------------------------------")

