#!/usr/bin/env python3

"""
Testing some code for fun - Shane's latest update.
Now I'm putting it through the Pylint suggestions to clean it up.
"""

import random

def magic_ball(tumbler):
    """Shane's using a list  instead of a long 'if, elif return' way of doing it like I was."""

    answer = ['It is certain.','It is decidedly so.','Yes',
              'Reply hazy, try again','Ask again later','Concentrate and ask again',
              'My reply is no.','Outlook not so good','Very doubtful']

    fortune = random.choice(answer)

    tumbler = fortune

    return tumbler

print(magic_ball(''))
