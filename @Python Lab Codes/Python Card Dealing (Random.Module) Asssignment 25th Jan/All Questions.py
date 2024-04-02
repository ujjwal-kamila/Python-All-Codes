# All Ans of Python assignment on Random Module 

import random

# Part 1
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

class CardDealer:
    def __init__(self):
        self.deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

    def deal_hand(self):
        print("Dealing ...")
        hand = random.sample(self.deck, 5)
        for card in hand:
            self.deck.remove(card)
        return hand

    def display_deck(self):
        print(self.deck)
        print(f"There are {len(self.deck)} cards in the deck.")

# Part 2
dealer = CardDealer()
dealer.display_deck()
hand = dealer.deal_hand()
print(f"There are {len(dealer.deck)} cards in the deck.")
print("Player has the following cards in their hand:")
print(hand)

# Part 3

try:
    with open("Text1.txt", "w") as file:
        dealer = CardDealer()
        for card in dealer.deck:
            file.write(card + "\n")
    print(f"Total number of lines in Text1.txt: {len(dealer.deck)}")

    with open("Text1.txt", "r") as file:
        cards_dict = {i: line.strip() for i, line in enumerate(file)}
        print(cards_dict)

except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error occurred: {e}")

# Part 4
try:
    with open("Text1.txt", "r") as file:
        cards_list_of_tuples = [(i, line.strip()) for i, line in enumerate(file)]
        print(cards_list_of_tuples)
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error occurred: {e}")
