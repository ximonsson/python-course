"""
Description:
    In this script we will read the input from "sequence.txt" and factorize the value on each
    line, but instead of printing the result to the console we will write each result on a
    separate line.
"""
from mathfuncs import fact

# open the input file in default read mode
f = open("sequence.txt")

# open the output file in write mode
# NOTE: we have to give the second "w" parameter for writing
fout = open("results.txt", "w")

# loop over each line in f
# factorize the result and then write it to the file
# NOTE: that the output of fact is an int and the write function requires a str.
#       we therefore need to cast the result to a str to give as input to write
# NOTE: we need to concatenate the str value that we are writing to file with "\n"
#       if we want it to appear on separate lines.
for line in f:
    x = fact(int(line))
    fout.write(str(x) + "\n")

# !! IMPORTANT !! to close the files when done
f.close()
fout.close()
