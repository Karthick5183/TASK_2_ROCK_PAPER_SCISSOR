# TASK_2_ROCK_PAPER_SCISSOR
# ROCK-PAPER-SCISSOR GAME

## AIM :
The aim of the Rock Paper Scissors game is to create a simple, interactive, and fun program that allows a user to play the classic Rock Paper Scissors game against the computer. The game randomly selects a move for the computer and compares it with the user's move to determine the winner. This project helps in understanding basic Python programming concepts such as input/output, random number generation, conditionals, and loops.
## ALGORITHM :
### STEP -1 
   Import Required Modules: We'll use the random module to allow the computer to make a random choice.
### STEP -2    
   Define the Game Rules: Establish the rules of Rock-Paper-Scissors.
### STEP -3 
    Get User Input: Prompt the user to enter their choice.
### STEP -4 
   Generate Computer Choice: Use the random module to generate a choice for the computer.
### STEP -5 
   Determine the Winner: Compare the user's choice with the computer's choice and determine the winner based on the game rules.
### STEP -6 
   Display the Result: Show the choices made and the result of the game.
### STEP -7 
   Replay Option: Optionally, allow the user to play multiple rounds.

## PROGRAM :
```python
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


```
## OUTPUT :
![](./WhatsApp%20Image%202024-06-02%20at%2023.06.43_c61ebb82.jpg)

## RESULT :
 Hence ,the ROCKPAPERSCISSOR game is successfully executed.
