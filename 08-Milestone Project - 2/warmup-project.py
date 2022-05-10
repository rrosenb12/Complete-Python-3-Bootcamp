# from unittest.util import three_way_cmp
import random

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card:
    # Each card has a suit, rank, and value
    # We don't need user to produce a value since we will have a dictionary of values to figure it out automatically
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

""" two_hearts = Card("Hearts","Two")
print(two_hearts)
# Two of Hearts
print(two_hearts.value)
# 2

three_of_clubs = Card("Clubs","Three") """

class Deck:
    # Instantiate new deck with all 52 card objects -> hold as a list of card objects
    ## This means the deck class will return card class object instances
    # Shuffle a Deck through method call
    # Deal cards from the deck object
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                # create the card object
                self.all_cards.append(created_card)
                
    # Doesn't happen immediately because not in __init__ -> need to call it
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

new_deck = Deck()

first_card = new_deck.all_cards[0]
print(first_card)

new_deck.shuffle()

first_card = new_deck.all_cards[0]
print(first_card)

my_card = new_deck.deal_one()

print(my_card)

# Will be 51 because we dealt 1
print(len(new_deck.all_cards))