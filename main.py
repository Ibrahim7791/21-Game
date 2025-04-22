# Author: Muhammad Ibrahim Qaiser

import random
# Assign the suits and values of each card into variables (dealing with Ace later)
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
ranks = [
    ("Ace", 11), ("2", 2), ("3", 3), ("4", 4), ("5", 5),
    ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10),
    ("Jack", 10), ("Queen", 10), ("King", 10)
]
# Create a list od the deck with every card
deck = []
for suit in suits:
    for rank, value in ranks:
        deck.append((f"{rank} of {suit}"))
# Shuffle the deck
random.shuffle(deck)
# The amount of players inputted by the user vs AI
players = []
for i in range(int(input("How many players? (Max 7)"))):
    # Creating "Player 1", "Player 2", etc
    players.append(f"Player {i+1}")
# Dealers first card
dealerCard = [deck.pop()]

# Give each player their first card
while True:
    print("The dealer's first card is face-down")
    # Give each player their first card
    for player in players:
        print(f"Player {player} 's first card is {deck.pop()}") # Make sure evry card is used once
    print("Round 2")
    # end loop
    break

#Assign second cards
while True:
    # Dealears second card (face-up)
    dealerCard2 = deck.pop()
    print(f"The dealer's second card is {dealerCard2}")
    for player in players:
        print(f"Player {player} 's second card is {deck.pop()}")
    break


    
while True:
    print("The dealer's first card is face-down")
    for player in players:
        print(f"Player {player} 's first card is {deck.pop()}")
    print("Round 2")
    break

while True:
    dealerCard2 = deck.pop()
    print(f"The dealer's second card is {dealerCard2}")
    for player in players:
        print(f"Player {player} 's second card is {deck.pop()}")
    break

