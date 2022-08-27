#!/bin/bash

# Infrastructure Engineer Academy 
# Session 1 Self-Paced Week:  Linux Exercises
# Curtis Roy, n0174972

# Determine if file(s) exist, error if not
# Append note to existing file(s)
# Remove empty files

if [[ -z "${1:-}" ]]; then
   printf "Argument expected.  Include valid filename.\n"
   printf "Valid names are file<1-3>.txt and empty<1-3>.rtf.\n"
fi

for item in "$@"; do
   if [[ ! -e "$item" ]]; then
      echo "Filename '$item' does not exist." 
   elif [[ ! -s $item ]]; then
      echo "Empty file.  Removing."
      rm "$item"
   else 
      echo "File exists and inspected."
      echo "Inspected by Curtis" >> "$item"
   fi
done