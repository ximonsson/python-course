"""
Description:
    This script takes the first command line argument sent to it and factorizes it before
    printing the result to console.

    Note that the script crashes in case we are sending any extra parameters or in case
    we give something else than an integer value. As an optional exercise try to catch
    the exceptions and handle them so it does not crash.
"""
import sys
from mathfuncs import fact

# exercise: put this within a try clause so you do not get errors in case the user forgets
# to enter an extra argument, or enters something that can not be translated to int

# take the second argument from the argv list
x = sys.argv[1]

# factorize the value (after casting to int) and print the result.
x = fact(int(x))
print(" >", x)
