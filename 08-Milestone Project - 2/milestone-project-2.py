# OOP BlackJack #

# Player starts with two cards face up
# Dealer starts with 1 card face up and 1 card face down
# Player goes first
# Player goal is to get closer to total value of 21 before dealer does
# Player can hit, to receive another card, or stand, to not receive any cards
# After player turn, if the player is under 21, dealer hits until they beat the player or bust
# If player keeps hitting over 21 before dealer goes, they bust and lose the bet
# Game is over and dealer collects money

# Face cards count as value of 10
# Aces can count as 1 or 11, whichver is preferable to player

import random

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
playing = True

## CLASSES ##

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
                card = Card(suit,rank)
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self):
        return f'I have {len(self.deck)} cards'

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

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet 

    def lose_bet(self):
        self.total -= self.bet

## FUNCTIONS ##

def take_bet(chips):
    valid_bet = False
    while not valid_bet:
        try:
            chips.bet = int(input("What would you like to bet? "))
        except ValueError:
            print("That's not a number! Try again.")
            continue
        else:
            if chips.bet > player_chips.total:
                print("You can't bet more than 100. Try Again.")
                continue
            elif chips.bet <= 0:
                print("You can't bet negative numbers, and you can't bet 0! Try again.")
                continue
            else:
                player_chips.bet = chips.bet
                valid_bet = True

def hit(hand,deck):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    while True:
        user_choice = input("Would you like to hit or stand? ")
        if user_choice[0].lower() == "h":
            hit(hand,deck)
        elif user_choice[0].lower() == "s":
            print("Player stands, dealer's turn")
            playing = False
        else:
            print("Sorry, please choose Hit or Stand")
            continue 
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push():
    print("Dealer and Player tie! It's a push.")

## GAME PLAY ##
    
while True:

    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(dealer_hand,deck)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)

        else:
            push()        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break