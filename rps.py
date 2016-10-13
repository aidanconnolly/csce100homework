import os
import random

p1wins = 0
p2wins = 0

choices = ["rock", "paper", "scissors"]

def choice():
    return random.choice(choices)

winner = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def result(player1, player2):
    global p1wins
    global p2wins
    if player1 == player2:
        print("Tie!")
        print("Player 1: %s, Player 2: %s\n" % (p1wins, p2wins))
    elif winner[player1] == player2:
        print("Player 1 wins!")
        p1wins += 1
        print("Player 1: %s, Player 2: %s\n" % (p1wins, p2wins))
    else:
        print("Player 2 wins!")
        p2wins += 1
        print("Player 1: %s, Player 2: %s\n" % (p1wins, p2wins))

os.system('clear')
mode = input("How would you like to play? (1, 2, or 3)\n1. Player versus Player\n2. Player versus Computer\n3. Computer versus Computer\n") 
print("\n")
if mode == "1":
    while p1wins != 2 and p2wins != 2:
        os.system('clear') 
        player1 = input("Player 1: Please pick 'rock' 'paper' or 'scissors'\n")
        os.system('clear')
        player2 = input("Player 2: Please pick 'rock' 'paper' or 'scissors'\n")
        os.system('clear')
        print("Player 1 picked ", player1)
        print("Player 2 picked ", player2)
        result(player1, player2)
        input("Press enter to continue: ")
    print("Game over!")
elif mode == "2":
    while p1wins != 2 and p2wins != 2:
        os.system('clear')
        player1 = input("Please pick 'rock' 'paper' or 'scissors'\n")
        player2 = choice()
        print("Player 2 picked", player2)
        result(player1, player2)
        input("Press enter to continue: ")
    print("Game over!")
elif mode == "3":
    while p1wins != 2 and p2wins != 2:
        os.system('clear') 
        player1 = choice()
        player2 = choice()
        print("Player 1 picked", player1)
        print("Player 2 picked", player2)
        result(player1, player2)
        input("Press enter to continue: ")
    print("Game over!")
else:
    print("Please choose 1, 2, or 3.")


