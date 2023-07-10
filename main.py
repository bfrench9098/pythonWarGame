#
# This program will simulate a game of War between the user and the computer
#

import random

# The Deck class is used to generate the initial deck of cards and give each card a
#   "value". The value will be used later when cards are being compared from draw
#   to draw.
#
# This class also holds utility functions for cutting the initial deck etc.
#
class Deck:
    
    SUITES = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    
    DECK = []
    
    def __init__(self) -> None:
        self.generate_deck()
        
        card_count = len(self.DECK)
        print("Have generated a new deck of {} cards.".format(card_count))
        #print(self.DECK)

        self.shuffle_deck()
        print("Deck has been shuffled.")
        #print(self.DECK)
        
    def generate_deck(self):
        suite_val = 0
        rank_val = 0

        for suite in self.SUITES:
            suite_val = suite_val + 1
            rank_val = 0

            for rank in self.RANKS:
                rank_val = rank_val + 1

                card_type = rank + suite
                card_val = rank_val + suite_val

                card = {card_type: rank_val}

                self.DECK.append(card)
        
    def shuffle_deck(self):
        random.shuffle(self.DECK)

# The Player class is used to hold player related information as well as the player's
#   cards after retrieving from the initial deck of cards generated in the Deck class.
#
# This class will also be used to hold some statistical items like number of hands won,
#   number of wins in a rwo, etc.
#
class Player:
    def __init__(self, name, draw):
        self.name = name
        self.draw = draw
        self.player_deck = []

    def draw_cards(self):
        self.player_deck.clear()

        i = 0

        for card in Deck.DECK:
            i = i + 1
            if self.draw == "even":
                if i % 2 == 0:
                    self.player_deck.append(card)
            elif self.draw == "odd":
                if i % 2 != 0:
                    self.player_deck.append(card)

# The actual game code starts here
#

# Generate the initial deck of cards and shuffle the deck
Deck()

# Set-up the computer player
computer = Player("Computer", "odd")
computer.draw_cards()

print("Welcome to WAR!!\n")

# Set-up the human opponent
player_name = input("Enter Your Name:  ")
opponent = Player(player_name, "even")
opponent.draw_cards()

print("S T A R T I N G    G A M E\n")
