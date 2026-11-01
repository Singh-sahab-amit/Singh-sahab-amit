import random
choice = ["rock","paper","scissor"]
player = input("Choose rock, paper, scissor: ").lower()
computer = random.choice(choice)

if player == computer:
    print(f"it is tie! Both choose{player}.")
elif (
    (player == "rock" and computer == "scissors") or  
    (player == "paper" and computer == "rock") or 
    (player == "scissor" and computer == "paper")
):
    print(f"you win!{player} beats {computer}.") 
else:
    print(f"computer win!{computer} beats {player}.")
