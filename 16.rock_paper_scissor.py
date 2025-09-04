import random

rock = ''' Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = ''' Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = ''' scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
a = ["rock" , "paper" , "scissors"]
diagram = [rock,paper,scissors]

#user : 
user = int(input("Press '0' for rock , '1' for paper , '2' for scissors: "))
if user > 2 or user <0 :
    print("Invalid input please retry.")
    exit()
else:
    print(f"You choose : {diagram[user]}.")


#computer :
comp = random.randint(0,2)
print(f"Computer choose : {diagram[comp]}.")

#rules :
if user == comp:
    print("It's a Draw.")
elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1):
    print("You Won!")
else:
    print("Computer Won!")
