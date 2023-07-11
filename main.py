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
        # print(self.DECK)

        self.shuffle_deck()
        print("Deck has been shuffled.")
        # print(self.DECK)

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
        self.war_wins = 0

    # Return the player name attribute
    def get_name(self):
        return self.name

    # draw 26 cards from Deck.DECK
    def draw_starting_cards(self):
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

    # Add 1 to WAR wins
    def add_war_win(self):
        self.war_wins = self.war_wins + 1

    def get_remaining_cards(self):
        return len(self.player_deck)

    # Draw one card from the top of player deck
    def draw_one(self):
        return self.player_deck.pop(0)

    def draw_three(self):
        three_cards = []
        i = 0

        while i < 3:
            three_cards.append(self.draw_one())
            i = i + 1

        return three_cards

    def draw_remaining(self):
        remaining_cards = []

        remaining_count = self.get_remaining_cards()

        i = 0

        while i < remaining_count:
            remaining_cards.append(self.draw_one())
            i = i + 1

        return remaining_cards


    # Append won cards to bottom of player deck
    def append_card(self, card):
        self.player_deck.append(card)


# Do a WAR (recursive method)
def do_war(computer_card, opponent_card, existing_war_chest = []):
    war_chest = []

    for card in existing_war_chest:
         war_chest.append(card)

    # Continue the WAR if each player has enough cards.
    #   Otherwise, the cards of the player without
    #   enough cards to continue go to the opposing
    #   player. This will end the game when the
    #   game complete check is done
    if computer.get_remaining_cards() < 4:
        print("Computer does not have enough cards to continue({}). {} wins the WAR!\n".format(computer.get_remaining_cards(), opponent.get_name()))
        opponent.append_card(computer_card)
        opponent.append_card(opponent_card)
        remaining_cards = computer.draw_remaining()
        for card in remaining_cards:
            war_chest.append(card)
        for card in war_chest:
            opponent.append_card(card)
        opponent.add_player_win()
        opponent.add_war_win()
    elif opponent.get_remaining_cards() < 4:
        print("{} does not have enough cards to continue({}). Computer wins the WAR!\n".format( opponent.get_name(), opponent.get_remaining_cards()))
        computer.append_card(computer_card)
        computer.append_card(opponent_card)
        remaining_cards = opponent.draw_remaining()
        for card in remaining_cards:
            war_chest.append(card)
        for card in war_chest:
            computer.append_card(card)
        computer.add_player_win()
        computer.add_war_win()
    else:
        war_chest.append(computer_card)
        war_chest.append(opponent_card)

        computer_draw_three = computer.draw_three()
        opponent_draw_three = opponent.draw_three()

        for card in computer_draw_three:
            war_chest.append(card)
        for card in opponent_draw_three:
                war_chest.append(card)

        computer_war_card = computer.draw_one()
        opponent_war_card = opponent.draw_one()

        keys = list(computer_war_card.keys())
        computer_war_card_key = keys[0]
        values = list(computer_war_card.values())
        computer_war_card_val = values[0]

        keys = list(opponent_war_card.keys())
        opponent_war_card_key = keys[0]
        values = list(opponent_war_card.values())
        opponent_war_card_val = values[0]

        print("Computer Drew a: {}\t\t{} Drew a: {}\n".format(computer_war_card_key, opponent.get_name(), opponent_war_card_key))

        if computer_war_card_val == opponent_war_card_val:
            print("W  A  R  !\n")
            do_war(computer_war_card, opponent_war_card, war_chest)
        elif computer_war_card_val > opponent_war_card_val:
            print("Computer Wins the WAR!\n")
            computer.add_player_win()
            computer.add_war_win()
            computer.append_card(computer_war_card)
            computer.append_card(opponent_war_card)
            for card in war_chest:
                computer.append_card(card)
        else:
            print("{} Wins the WAR!\n".format(opponent.get_name()))
            opponent.add_player_win()
            opponent.add_war_win()
            opponent.append_card(computer_war_card)
            opponent.append_card(opponent_war_card)
            for card in war_chest:
                opponent.append_card(card)

# Check the player decks to see if anyone has run out of cards. When either the computer
#   or the opponent run out of cards the game is over.
def game_complete():
    computer_remaining_cards = computer.get_remaining_cards()
    opponent_remaining_cards = opponent.get_remaining_cards()

    print("{} cards remaining: {}\tComputer cards remaining: {}\n".format(opponent.get_name(), opponent.get_remaining_cards(), computer.get_remaining_cards()))

    if computer_remaining_cards == 0:
        print("{} Wins the Game!\n".format(opponent.get_name()))

    if opponent_remaining_cards == 0:
        print("Computer Wins the Game!\n")

    if computer_remaining_cards == 0 or opponent_remaining_cards == 0:
        return True
    else:
        return False

# Do a hand
def do_hand():
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
        do_war(computer_card, opponent_card)
    elif computer_card_val > opponent_card_val:
        print("Computer Wins the Hand!\n")
        computer.add_player_win()
        computer.append_card(computer_card)
        computer.append_card(opponent_card)
    else:
        print("{} Wins the Hand!\n".format(opponent.get_name()))
        opponent.add_player_win()
        opponent.append_card(computer_card)
        opponent.append_card(opponent_card)


# The actual game code starts here
#

# Generate the initial deck of cards and shuffle the deck
Deck()

# globals
keep_going = True

# Set up the computer player
computer = Player("Computer", "odd")
computer.draw_starting_cards()

print("Welcome to WAR!!\n")

# Set up the human opponent
player_name = input("Enter Your Name:  ")
opponent = Player(player_name, "even")
opponent.draw_starting_cards()

print("\nS T A R T I N G    G A M E\n")

while keep_going is True:
    do_hand()
    if game_complete():
        keep_going = False

print("{} Statistics:\n".format(opponent.get_name()))
print("\tHands won:{}".format(opponent.player_wins))
print("\tWARs won: {}\n".format(opponent.war_wins))

print("Computer Statistics:\n")
print("\tHands won:{}".format(computer.player_wins))
print("\tWARs won: {}\n".format(computer.war_wins))