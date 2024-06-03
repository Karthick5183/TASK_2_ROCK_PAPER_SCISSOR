import random

options = ('rock', 'paper', 'scissors')
play = True

while play:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = str(input("Enter a choice (rock, paper, scissors): "))
        

    print(f"player: {player}")
    print(f"player: {computer}")

    if player == computer:
        print("Game is tie!")
        print("Game over")
    elif player == "rock" and computer == "scissors":
        print("You win!")
        print("Game over")
    elif player == "paper" and computer == "rock":
        print("You win!")
        print("Game over")
    elif player == "scissors" and computer == "paper":
        print("You win!")
        print("Game over")
    else:
        print("You lose!")
        print("Gmae over!")


    if not input("Play again? (yes/no): ").lower() == "yes":
        play = False

print("Thanks for playing!")