#Write a check input function
#print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

import random


#Prompting user on how to play
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

#trap user in a loop here
while True:
  print("'r' = Rock")
  print("'p' = Paper")
  print("'s' = Scissors")
  print()
  print("Please select a 'draw' or input q to quit:")
#Storing user's choice of rps
  mychoice = input()

#input check/translator
#checkinput() function should start here.
if mychoice != "r" or "p" or "s" or "q":
    print("Invalid input.")
    print("Please input either 'r','p' or 's' input 'q' to quit.")
    mychoice = input()
