""""
1 input from user(Rock,paper,scissor)
2 computer choice
3 result print

cases:
A- rock
rock rock= tie
paper paper= win
rock scissor= rock win

B- paper
paper paper=tie
paper rock=paper win
paper scissor= scissor win

c- scissor
scissor scissor=tie
scissor rock= rock win
scissor paper= scissor win
"""

import random
item_list=["Rock","Paper","Scissor"]
user_input=input("Enter your choice=Rock, Paper,Choice")
com_choice=random.choice(item_list)
print(f"user Choice={user_input},Computer Choice{com_choice}")
if user_input==com_choice:
    print("both Chooses same: Match Tie")
elif user_input=="Rock" and com_choice=="Paper":
    print("Paper covers rock: computer win")
elif user_input=="Rock" and com_choice=="Scissor":
    print("rock break scissor: user win")
else:
    print("valid input")
