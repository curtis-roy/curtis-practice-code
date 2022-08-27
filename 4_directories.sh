#!/bin/bash

# Infrastructure Engineer Academy 
# Session 1 Self-Paced Week:  Linux Exercises
# Curtis Roy, n0174972

# Goal:  Partition all the files into subdirectories based on the file extension.

#ls > filelist.txt # I think I might need this if I can figure out a better way.

# This works but doesn't deal with files that have no extension.

for filename in *; do
   if [[ -f "$filename" ]]; then
       base=${filename%.*}
       ext=${filename#"$base".}
     mkdir -p "${ext}"
     cp "$filename" "${ext}"
   fi
 done