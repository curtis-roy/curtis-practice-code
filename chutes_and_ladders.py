#!/usr/bin/env python3

"""An adaptation of the board game of the same name
Obtained from http://rosettacode.org/wiki/chute_and_ladder#Python
Cleaned up with Pylint suggestions
"""

import random
import sys

snl = {
    4: 14,
    9: 31,
    17: 7,
    20: 38,
    28: 84,
    40: 59,
    51: 67,
    54: 34,
    62: 19,
    63: 81,
    64: 60,
    71: 91,
    87: 24,
    93: 73,
    95: 75,
    99: 78
}
SIXES_ROLL_AGAIN = True

def play(player, square):
    """Here's the mechanism of the game"""
    while True:
        roll = random.randint(1,6)
        sys.stdout.write("Player {0} on square {1}, rolls a {2}".format(player, square, roll))
    if square + roll > 100:
        print (" but cannot move.")
    else:
        square += roll
        print (" and moves to square {0}".format(square))
        if square == 100:
            return 100
        turn = snl.get(square, square)
        if square < turn:
            print ("Yay! landed on a ladder. Climb up to {0}.".format(turn))
            if square == 100:
                return 100
            square = turn
        elif square > turn:
            print ("Oops! Landed on a chute. Slide down to {0}.".format(turn))
            square = turn
    if roll < 6 or not SIXES_ROLL_AGAIN:
        return square
    print ("Rolled a 6 so roll again.")

def main():
    """Players"""
    players = [1, 1, 1]
    while True:
        for i in range(0, 3):
            n_s = play(i+1, players[i])
            if n_s == 100:
                print ("Player {0} wins!".format(i+1))
                return
            players[i] = n_s

main()
