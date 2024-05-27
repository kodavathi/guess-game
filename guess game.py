import random

number=random.randint(1, 200)
print("May I ask you for your name?")
name=input() #asks for the name
print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
print("Go ahead. Guess!")
playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
    guessTaken = 0
    while guessTaken < 6:
        g=input("Guess: ")
        try:
            guess=int(g)
            if guess<=200 and guess>=1:
                if guessTaken<6:
                    if guess<number:
                        print("The guess of the number that you have entered is too low")
                        print("Try Again!")
                    if guess>number:
                        print("The guess of the number that you have entered is too high")
                        print("Try Again!")
                if guess==number:
                    break
                guessTaken=guessTaken+1
            if guess>200 or guess<1:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 200")
        except:
            print("I don't think that "+enter+" is a number. Sorry")
    if guess == number:
        guessTaken = str(guessTaken)
        print('Good job, ' + name + '! You guessed my number in ' + guessTaken + ' guesses!')
    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))
    playagain=input("Do you want to play again?")
