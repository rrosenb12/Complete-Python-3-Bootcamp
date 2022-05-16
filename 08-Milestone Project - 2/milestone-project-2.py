# OOP BlackJack #

# Computetr dealer, human player
# Start with normal deck of cards
# Create representation of a deck

# Human player has a bank roll
## Attribute for bank roll (like a bank account)
## From bank roll, human player will place a bet depending on whether or not they will win the set of hands

# Player starts with two cards face up
# Dealer starts with 1 card face up and 1 card face down
# Player goes first
# Player goal is to get closer to total value of 21 before dealer does
# Player can hit, to receive another card, or stay, to not receive any cards
# After player turn, if the player is under 21, dealer hits until they beat the player or bust
# If player keeps hitting over 21 before dealer goes, they bust and lose the bet
# Game is over and dealer collects money

# Face cards count as value of 10
# Aces can count as 1 or 11, whichver is preferable to player

import random

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card:
    # Each card has a suit, rank, and value
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    # Instantiate new deck with all 52 card objects -> hold as a list of card objects
    ## This means the deck class will return card class object instances
    # Shuffle a Deck through method call
    # Deal cards from the deck object
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.deck.append(created_card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self):
        return f'I have {len(self.deck)} cards'

new_deck = Deck()
new_deck.shuffle()
"""
print(new_deck)
- returning "I have 52 cards"
print(new_deck.decj[0].value)
- returning [1,11] if Ace
print(len(new_deck.deck))
- returning 52
"""

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        return f'{self.cards}'

my_hand = Hand()
my_hand.add_card(new_deck.deal())
my_hand.add_card(new_deck.deal())
"""
for card in my_hand.cards:
    print(card)
- returning cards
print(my_hand.value)
- printing value of hand
"""

dealer_hand = Hand()
dealer_hand.add_card(new_deck.deal())
dealer_hand.add_card(new_deck.deal())
"""
print(dealer_hand.cards[0])
- returning first card
"""

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet 

    def lose_bet(self):
        self.total -= self.bet

my_chips = Chips()

def take_bet():
    valid_bet = False
    while not valid_bet:
        try:
            player_bet = int(input("What would you like to bet? "))
        except ValueError:
            print("That's not a number! Try again.")
            continue
        else:
            my_chips.bet = player_bet
            valid_bet = True
    
take_bet()