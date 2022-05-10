from unittest.util import three_way_cmp


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

two_hearts = Card("Hearts","Two")
print(two_hearts)
# Two of Hearts
print(two_hearts.value)
# 2

three_of_clubs = Card("Clubs","Three")