# from unittest.util import three_way_cmp
from hashlib import new
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

""" 
two_hearts = Card("Hearts","Two")
print(two_hearts)
# Two of Hearts
print(two_hearts.value)
# 2

three_of_clubs = Card("Clubs","Three") 
"""

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
# print(first_card)

new_deck.shuffle()

first_card = new_deck.all_cards[0]
# print(first_card)

my_card = new_deck.deal_one()

# print(my_card)

# Will be 51 because we dealt 1
## print(len(new_deck.all_cards))

class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0) 

    def add_cards(self,new_cards):
        # For multiple card objects -> extend adds list to list without nesting it. 
        ## For example:
        ### list = [a,b,c]
        ### new_list = [d,e,f]
        ### list.extend(new_list) = [a,b,c,d,e,f]
        ### vs
        ### list.append(new_list) = [a,b,c,[d,e,f]]
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        # For a single card object
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

"""
new_player = Player("Jose")
print(new_player)
# 0 cards
new_player.add_cards(my_card)
print(new_player)
# 1 card
print(new_player.all_cards[0])
new_player.add_cards([my_card, my_card, my_card])
print(new_player)
# 4 cards
new_player.remove_one()
print(new_player)
# 3 cards
"""

### GAME LOGIC ###

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

# Don't need to go through this 52 times since you're dealing two cards in each for loop to each player
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# print(len(player_one.all_cards))
## 26

game_on = True
round_number = 0

while game_on:

    round_number += 1
    print(f'Round {round_number}')

    # CHECK THAT PLAYER STILL HAVE CARDS #

    if len(player_one.all_cards) == 0:
        print("Player One out of cards, player Two wins!")
        game_on = False
        # Will automatically break out of loop once game_on is False
        # break
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards, player One wins!")
        game_on = False
        # break
    
    # START A NEW ROUND #

    # Different from all_cards; these are the cards currently in play
    player_one_cards = []
    # Takes one card from respective player's deck, becomes current card in play
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # Always assume a war, just so that the comparison can happen (even if there isn't an official war and it's just one card)
    at_war = True 
    
    while at_war:

        # If at official war, there are multiple cards currently in play for each player. If not at official war and regular game play, just one card in list. Check the last current card at play either way since game logic is relatively the same for both instances, just depends on if they draw more than 1 card at a time
        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        # This is the logic where an official war occurs
        else: 

            print("WAR!")

            if len(player_one.all_cards) < 5:
            
                print("Player One unable to war")
                print("Player Two wins!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:

                print("Player Two unable to war")
                print("Player One wins!")
                game_on = False
                break

            else:
                for num in range(5):

                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
