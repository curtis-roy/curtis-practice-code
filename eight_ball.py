#!/usr/bin/env python3

"""
Edited 08-04-2022 for style
Including common conventions for snake_case
as well as appropriate use of CAPS, etc. that were suggested by Pylint.
"""

import random

def get_answer(answer_number):
    """Replicates performance of a Magic 8 Ball toy."""
    if answer_number == 1:
        return '\nIt is Certain\n'
    elif answer_number == 2:
        return '\nIt is Decidedly So\n'
    elif answer_number == 3:
        return '\nYes\n'
    elif answer_number == 4:
        return '\nReply Hazy, Try Again\n'
    elif answer_number == 5:
        return '\nAsk Again Later\n'
    elif answer_number == 6:
        return '\nConcentrate and Try Again\n'
    elif answer_number == 7:
        return '\nMy Reply is No\n'
    elif answer_number == 8:
        return '\nOutlook Not so Good\n'
    elif answer_number == 9:
        return '\nVery Doubtful\n'

r = random.randint(1,9)
FORTUNE = get_answer(r)
print(FORTUNE)
