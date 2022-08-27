#!/bin/bash

# Infrastructure Engineer Academy 
# Session 1 Self-Paced Week:  Linux Exercises
# Curtis Roy, n0174972

# Goal:  Reverse the name of some files and then put them back.

clear

ls empty*.rtf > forwards && ls file*.txt >> forwards

printf "This will list files, rename them, then restore them.\n"
printf "Prerequsite: run 1_testfilesetup.sh first.\n"
printf "Original files:\n"
cat forwards
sleep 2
clear

tac forwards | rev > reversed

echo "Reversing files..."
sleep 1
paste -d " " forwards reversed | sed "s/^/mv /" | bash
cat reversed
printf "Filenames reversed.\n"
sleep 2
clear

echo "Restoring files..."
sleep 1
paste -d " " reversed forwards | sed "s/^/mv /" | bash
cat forwards
printf "Filenames restored.\n"

# cleanup
# rm forwards && rm reversed
