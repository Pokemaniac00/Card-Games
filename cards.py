#!/bin/env python

import random, re

VALUES = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
POINTS = ["special", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
SPECIAL = [1, 11]
SUITS = ["Spades", "Hearts", "Clubs", "Diamonds"]
deck = []

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.value + " of " + self.suit

def initialize_deck(decks):
    for i in range(0, decks):
        for suit in SUITS:
            for value in VALUES:
                deck.append(Card(value, suit))

def shuffle():
    """
        Performs a complete shuffle of the deck, also prompting the user to cut the deck.
    """
    global deck
    cards_string = str(len(deck))
    cards = len(deck)
    for i in range(0, 6):
        random.shuffle(deck)
    pivot = ""
    pivot = input("Choose a number from 0 to " + cards_string + " in which to cut the deck. (With 1 being the top of the deck and " + cards_string + " being the bottom. Inputting 0 or " + cards_string + " will leave the deck as is.): ")
    flag = False
    while not flag:
        try:
            tmp = int(pivot)
            if tmp >= 0 and cards >= tmp:
                flag = True
            if flag:
                break
        except TypeError:
            print("Please input a one or two digit number between 0 and " + cards_string)
        pivot = input("Choose a number from 0 to " + cards_string + " in which to cut the deck. (With 1 being the top of the deck and " + cards_string + " being the bottom. Inputting 0 or " + cards_string + " will leave the deck as is.): ")
    temp = []
    pivot = int(pivot)
    for card in range(pivot, len(deck)):
        temp.append(deck[card])
    for card in range(0, pivot):
        temp.append(deck[card])
    deck = temp

def main():
    decks = input("Welcome to Blackjack. How many decks would you like to play with today(1-8)? ")
    while not re.match("^[1-8]$", decks):
        decks = input("How many decks would you like to use today(1-8)? ")
    initialize_deck(int(decks))
    shuffle()
    i = 1
    graveyard = []

    while True:
        # Every 5 turns, reshuffle.
        if i % 5 == 0:
            print("Returning played cards to deck...")
            for k in range(0, len(graveyard)):
                deck.append(graveyard.pop())
            print("Shuffling deck...")
            shuffle()

        player = []
        dealer = []
        player.append(deck.pop())
        dealer.append(deck.pop())
        player.append(deck.pop())
        dealer.append(deck.pop())
        print("The dealer's top card is the " + dealer[1] + ".")
        print("You glance at your cards.")
        print(player[0], player[1])

        # Check the total value of the player's cards.
        ace_flag = False
        total = 0
        print("Totaling card points...")
        for i in range(0, len(player)):
            try:
                total += POINTS[int(VALUES.index(player[i].value))]
            except TypeError:
                total += 1
                ace_flag = True
        print("Done! With your hand, you have a total of " + str(total) + " points.")
        if(ace_flag and total + 10 <= 21):
            print("Or, with your ace as 11 points you also would have a total of " + str(total + 10) + " points")

        # TODO: Change this method name to blackjack()
        # TODO: add functionality for hit, stand, and split. Add insurance later.
        # Bet before even showing player cards.
        # Then after players turn, show the dealer hand and their points, then draw if points below certain number.
        # Later add functionality for betting.
        
        # TODO: Put everything into methods to emulate flow of the game. Awesome work today!
        # This application will be built on in many phases. First just being a command-line blackjack game.
        # Then moving towards other commandline card games.
        # Then starting to merge everything to GUI.
        # Then more support from there moving forward.
    
    # At the end of each turn, return the cards from the dealer and the player to be added and shuffled back into the deck(s) later.
    for j in range(0, len(player)):
        graveyard.append(player.pop)
    for j in range(0, len(dealer)):
        graveyard.append(player.pop)
    


main()