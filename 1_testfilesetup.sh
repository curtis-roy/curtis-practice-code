#!/bin/bash

# Infrastructure Engineer Academy 
# Side project to set up test files for "Session 1 Self-Paced Week:  Linux Exercises"
# Curtis Roy, n0174972

printf "\nThis is the lab enviroment for IEA Session 1 \"Self-Paced Linux Exercises\". \n"
printf "Three empty .rtf files and three non-empty .txt files will be created.  \n\n"

while true; do

read -r -p "Do you want to tear down (t) or build the test files? (b)?  Enter t or b. " tb

case $tb in 
    t ) echo "Removing lab files.  Ctrl-C within 3 sec to cancel."
    sleep 3
    echo "Removing..."
    rm empty*.rtf && rm file*.txt
    echo "Done."
        break;;
    b ) echo "Building test files..."
    sleep 1
    echo "Done."
    touch empty{1..3}.rtf && touch file{1..3}.txt && echo "not_empty" | tee file*.txt > /dev/null
        break;;
    * ) echo "Invalid entry."
esac

done