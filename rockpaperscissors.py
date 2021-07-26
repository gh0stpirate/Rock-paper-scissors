#Rock paper scissors test

#Write a check input function

#important code layout
#import random
#mylist = ["apple", "banana", "cherry"]
#print(random.choice(mylist))

import random

#Prompting user on how to play
print("'r' = Rock")
print("'p' = Paper")
print("'s' = Scissors")
print()
print("Please select a 'draw' or input q to quit:")
#Storing user's choice of rps
mychoice = input()

#input check/translator
#checkinput() function should start here.
if mychoice != "r" or "p" or "s":
    print("Invalid input.")
    print("Please input either 'r','p' or 's' input 'q' to quit.")
    mychoice = input()

if mychoice == "r":
    mychoice = "rock"

if mychoice == "p":
    mychoice = "paper"

if mychoice == "s":
    mychoice = "scissors"

if mychoice == "q":
    print("Quitting...")
    quit()

#generating cpu's choice
cpuchoicelist = ["rock", "paper", "scissors"]
cpupick = random.choice(cpuchoicelist)

#laying out the hands
print(f"You chose: {mychoice}")
print(f"Computer chose: {cpupick}")

#decision logic here in order: rock, then paper, then scissors.
if mychoice == "rock" and cpupick == "scissors":
    print("rock smashes scissors.")
    print("You win!")

if mychoice == "rock" and cpupick == "paper":
    print("paper covers rock.")
    print("You loose! :(")

if mychoice == "rock" and cpupick == "rock":
    print("The rocks smash together. It's an even draw.")

if mychoice == "paper" and cpupick == "rock":
    print("paper covers rock.")
    print("You win!")

if mychoice == "paper" and cpupick == "paper":
    print("Both the papers fold over.")
    print("It's a draw.")

if mychoice == "paper" and cpupick == "scissors":
    print("scissors cut paper.")
    print("You loose!")

if mychoice == "scissors" and cpupick == "rock":
    print("rock smashes scissors.")
    print("You loose!")        

if mychoice == "scissors" and cpupick == "paper":
    print("scissors cut paper.")
    print("You win!")    

if mychoice == "scissors" and cpupick == "scissors":
    print("The scissors glance off one another.")
    print("It's a draw!")    