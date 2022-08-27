#!/usr/bin/env python3

"""A countdown timer."""

import time

def countdown(tictoc):
    """Incrementing seconds down by one."""
    while tictoc:
        mins, secs = divmod(tictoc, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        tictoc -= 1
    print("Break's over.")

t = input("Enter the time in seconds: ")

countdown(int(t))
