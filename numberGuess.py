import random
randNumber = random.randint(1,100)
# print(randNumber)
userGuess = None
guesses = 0


print("Choose a number between 1 to 100")
while(userGuess != randNumber):
    userGuess = int(input("Enter Your Guess:  "))
    guesses += 1
    if(userGuess == randNumber):
        print("Congrats !! You Guessed It Right !!")
    else:
        if(userGuess>randNumber):
            print("SORRY !! You Guessed It Wrong !  Please Enter a Smaller Number")
        else:
             print("SORRY !! You Guessed It Wrong !  Please Enter a Larger Number")

print(f"You Guessed the number in {guesses} attempts.")
