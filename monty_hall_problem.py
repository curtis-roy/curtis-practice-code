#!/usr/bin/env python3

"""
A solution to the Monty Hall Problem I found at rosettacode.org, formatting cleaned up with Pylint
"""

import random
 #1 represents a car
 #0 represent a goat

STAY = 0  #amount won if STAY in the same position
SWITCH = 0 # amount won if you SWITCH

for i in range(1000):
    lst = [1,0,0]           # one car and two goats
    random.shuffle(lst)     # shuffles the list randomly

    ran = random.randrange(3) # gets a random number for the random guess

    user = lst[ran] #storing the random guess
    del lst[ran] # deleting the random guess
    HUH = 0
    for i in lst: # getting a value 0 and deleting it
        if i ==0:
            del lst[HUH] # deletes a goat when it finds it
            break
        HUH+=1

    if user ==1: # if the original choice is 1 then STAY adds 1
        STAY+=1

    if lst[0] == 1: # if the switched value is 1 then SWITCH adds 1
        SWITCH+=1

print("Stay =",STAY)
print("Switch = ",SWITCH)
