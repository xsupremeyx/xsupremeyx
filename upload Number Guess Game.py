'''Make a Program in which a number will be specified and the
 user will guess the number through inputs, if the input is less or greater than
the number then tell the user so, so that they can correct themselves
there are 9 tries in total, and with every failed guess, print no. of
guesses left, if it becomes 0 print game over
number= 18'''
jackpot=int(18)
attempts=int(0)
guess=int(0)
while (True):
    guess=(int(input("Enter your Guess for the Jackpot number : ")))
    attempts+=1
    tries=9-attempts
    if tries==0:
        print("Uh oh!, You have 0 tries left now,\n Game Over!")
        break
    elif guess==18:
        print("Congratulations!\n You Guessed the Jackpot in",attempts,"attempt(s)!")
        break
    elif guess<18:
        print("The Number is Less than the Jackpot.\n Try Again!")
        print("You have",tries,"Attempts left\n")
        continue
    elif guess>18:
        print("The Number is More than the Jackpot.\n Try Again")
        print("You have", tries, "Attempts left\n")
        continue
    else:
        print("Unexpected Error,\n Play Again")


