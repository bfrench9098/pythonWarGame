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
    # init method
    def __init__(self, name, draw):
        self.name = name
        self.draw = draw
        self.player_deck = []
        self.player_wins = 0

    # Return the player name attribute
    def get_name(self):
        return self.name

    # draw 26 cards from Deck.DECK
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

    # Add 1 to player wins
    def add_player_win(self):
        self.player_wins = self.player_wins + 1

    def get_remaining_cards(self):
        return len(self.player_deck)

    # Draw one card from the top of player deck
    def draw_one(self):
        return  self.player_deck.pop(0)

    def draw_three(self):
        three_cards = []
        i = 0

        while i < 3:
            three_cards.append = self.player_deck.pop(0)
            i = i + 1

        return three_cards

    # Append won cards to bottom of player deck
    def append_cards(self, cards):
        self.player_deck.append(cards)

# Do a WAR
def do_war():
    pass

# Check the player decks to see if anyone has run out of cards. When either the computer
#   or the opponent run out of cards the game is over.
def game_complete():
    computer_remaining_cards = computer.get_remaining_cards()
    opponent_remaining_cards = opponent.get_remaining_cards()

    if computer_remaining_cards == 0:
        print("{} Wins the Game!".format(opponent.get_name()))

    if opponent_remaining_cards == 0:
        print("Computer Wins the Game!")

    if computer_remaining_cards == 0 or opponent_remaining_cards == 0:
        return True
    else:
        return False

def do_hand():
    computer_card = []
    opponent_card = []

    computer_card = computer.draw_one()
    opponent_card = opponent.draw_one()

    keys = list(computer_card.keys())
    computer_card_key = keys[0]
    values = list(computer_card.values())
    computer_card_val = values[0]

    keys = list(opponent_card.keys())
    opponent_card_key = keys[0]
    values = list(opponent_card.values())
    opponent_card_val = values[0]

    print("Computer Drew a: {}\t\t{} Drew a: {}\n".format(computer_card_key, opponent.get_name(), opponent_card_key))

    if computer_card_val == opponent_card_val:
        print("W  A  R  !\n")
        do_war()
    elif computer_card_val > opponent_card_val:
        print("Computer Wins the Hand!\n")
        computer.add_player_win()
        computer.append_cards(computer_card)
        computer.append_cards(opponent_card)
    else:
        print("{} Wins the Hand!\n".format(opponent.get_name()))
        opponent.add_player_win()
        opponent.append_cards(computer_card)
        opponent.append_cards(opponent_card)

# The actual game code starts here
#

# Generate the initial deck of cards and shuffle the deck
Deck()

#globals
keep_going = True

# Set up the computer player
computer = Player("Computer", "odd")
computer.draw_cards()

print("Welcome to WAR!!\n")

# Set up the human opponent
player_name = input("Enter Your Name:  ")
opponent = Player(player_name, "even")
opponent.draw_cards()

print("\nS T A R T I N G    G A M E\n")

while keep_going is True:
    do_hand()
    if game_complete():
        keep_going = False



