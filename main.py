# Author: Muhammad Ibrahim Qaiser

import random

suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
ranks = [
    ("Ace", 11), ("2", 2), ("3", 3), ("4", 4), ("5", 5),
    ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10),
    ("Jack", 10), ("Queen", 10), ("King", 10)
]
deck = []
for suit in suits:
    for rank, value in ranks:
        deck.append((f"{rank} of {suit}"))

random.shuffle(deck)

players = []
for i in range(int(input("How many players? (Max 7)"))):
    players.append(f"Player {i+1}")

dealerCard = [deck.pop()]
    
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

