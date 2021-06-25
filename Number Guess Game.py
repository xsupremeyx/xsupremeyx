print("This is a number guess game", end ='. ')
print("Try to guess the jackpot number")
print("IF your guess was MORE than the jackpot, then the jackpot will be LESS than that guess")
print("IF your guess was LESS than the jackpot, then the jackpot will be MORE than that guess")
print("To Play the game, Follow the instructions Carefully, Do NOT ENTER ANYTHING ELSE THAN WHOLE NUMBERS, Even Spaces\n")
import random
jackpot=random.randint(0,100)
attempts=int(0)
guess=int(0)
while (True):
    guess=(int(input("Enter your Guess for the Jackpot number (100 or lower) :\n ")))
    if guess>100:
        print("Too Large Number, Try Again\n")
        continue
    else:
        attempts += 1
        tries = 9 - attempts
        if tries==0:
            print("Uh oh!, You have 0 tries left now, Correct Answer was",jackpot,"\n Game Over!")
            break
        elif guess==jackpot:
            print("Congratulations!\n You Guessed the Jackpot in",attempts,"attempt(s)!\n")
            print("Press Y To Play Again or N To Exit")
            game=str(input("\n"))
            game=game.upper()
            if game=="Y":
                print("Restarting Game\n")
                continue
            else:
                print("Terminated")
                break
        elif guess<jackpot:
            print("Your Number is Less than the Jackpot.\n Try Again!")
            print("You have",tries,"Attempts left\n")
            continue
        elif guess>jackpot:
            print("Your Number is More than the Jackpot.\n Try Again")
            print("You have", tries, "Attempts left\n")
            continue
        else:
            print("Unexpected Error,\n Play Again")

