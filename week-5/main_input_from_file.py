"""
Description:
    This script will read every line in 'sequence.txt' and factorize the value on it and then
    print it out to console.

    As an optional exercise try making the script take as a command line argument of the file
    that it should read for input.
"""
from mathfuncs import fact

# Exercise: make the script read a command line argument that is the name of the file with data

# open the file - default mode is reading in text mode
f = open("sequence.txt")

# loop over each line and cast it to an int, then print the result of factorizing it to console
for line in f:
    x = fact(int(line))
    print(" >", x)

f.close() # !! IMPORTANT !!
