# Write a function that computes the volume of a sphere given its radius.

from ast import Return
from cmath import pi

def vol(rad):
    volume = (4/3*(pi*rad**3))
    return(volume)

vol(2)

# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    my_list = list(range(low,high+1))
    if num in my_list:
        return(num,True)
    else:
        return(False)

ran_check(5,2,7)

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(s):
    low = 0
    up = 0

    for letter in s:
        if letter.isupper():
            up += 1
        elif letter.islower():
            low += 1
    
    return(low,up)

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

# Write a Python function to multiply all the numbers in a list.

def multiply(numbers):  
    result = 1
    for number in numbers:
        result = result * number

    return(result)

multiply([1,2,3,-4])

# Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(s):
    no_space = s.replace(" ", "")
    backwards_s = no_space[::-1]
    return no_space == backwards_s

palindrome('helleh')

# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alpha_list = list(alphabet)
    no_space = str1.replace(" ","").lower()
    for letter in no_space:
        for idx in range(len(alpha_list)):
            if alpha_list[idx] == letter:
                alpha_list.pop(idx)
                break
            else:
                continue
    if len(alpha_list) == 0:
        return("panagram")
    
ispangram("The quick brown fox jumps over the lazy dog")