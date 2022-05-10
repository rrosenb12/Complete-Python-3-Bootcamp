### Problem 1
## Handle the exception thrown by the code below by using try and except blocks.

from tokenize import String
from typing import Type


for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError:
        print("You can't square a letter")
        break

### Problem 2
## Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

x = 5
y = 0

try:    
    z = x/y
except ZeroDivisionError:
    print("You can't divide by 0")
finally:
    print("All Done")

### Problem 3
## Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    user_input = ''
    while type(user_input) == str:
        try:
            val = int(input("Please enter an integer: "))
        except: 
            print("That is not an integer")
            continue 
        else:
            user_input = val
            print("Your number squared is: ", user_input**2)

ask()