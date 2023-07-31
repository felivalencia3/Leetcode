#!/usr/bin/env bash
FILE="neet_list.txt"
LINES=312

# Generate a random number between 1 and the number of lines
RANDOM_LINE=$((1 + RANDOM % LINES))

# Use sed to print the line corresponding to the random number
sed -n "${RANDOM_LINE}p" $FILE
