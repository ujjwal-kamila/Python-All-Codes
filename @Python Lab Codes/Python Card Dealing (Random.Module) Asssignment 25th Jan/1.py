import random

# Define the suits and ranks for the deck
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# Part 1: Create functions for deck creation, dealing, and display
def create_deck():
    # Use list comprehension to create a deck with all combinations of suits and ranks
    return [f"{rank} of {suit}" for suit in suits for rank in ranks]

def deal_hand(deck):
    print("Dealing ...")
    # Use random.sample to deal 5 random cards
    hand = random.sample(deck, 5)
    for card in hand:
        deck.remove(card)  # Remove dealt cards
    return hand

def display_deck(deck):
    print(deck)
    print(f"There are {len(deck)} cards in the deck.")

# Part 2: Create and display the initial deck, deal a hand, and display the updated deck
deck = create_deck()
display_deck(deck)
hand = deal_hand(deck)
print(f"There are {len(deck)} cards in the deck.")
print("Player has the following cards in their hand:")
print(hand)

# Part 3: Write the deck to a file, count lines, and read into a dictionary
try:
    with open("Text1.txt", "w") as file:
        deck = create_deck()  # Re-create the deck for writing to the file "Text1.txt"
        for card in deck:
            file.write(card + "\n")  # Write each card to a new line
    print(f"Total number of lines in Text1.txt: {len(deck)}")

    with open("Text1.txt", "r") as file:
        cards_dict = {i: line.strip() for i, line in enumerate(file)}
        print(cards_dict)

except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error occurred: {e}")

# Part 4: Read the file into a list of tuples
try:
    with open("Text1.txt", "r") as file:
        # Use enumerate to get line numbers and to create a list of tuples with line number and card
        cards_list_of_tuples = [(i, line.strip()) for i, line in enumerate(file)]
        print(cards_list_of_tuples)
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"An error occurred: {e}")
