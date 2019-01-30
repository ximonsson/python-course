"""
Description:
    This script will halt and ask the user to input a value to factorize, which is then
    printed to the console.

    Note how we are not guarding against exceptions in case the user inputs anything other
    than an integer value.

    As an optional exercise you can try and complement this script with a while-loop that keeps
    the application alive until the user type "quit". This is done by putting the code that calls
    'input' within a while-loop that runs forever (while True) and if the return value of
    input equals "quit" then break.
"""
from mathfuncs import fact

# exercise:
#	put the below code within a while loop that goes on forever until the user types "quit"

# read input from user
# the program halts here until the user inputs something
x = input("enter a value to factorize: ")

# factorize the value (after casting to int) and print the result.
x = fact(int(x))
print(" >", x)
