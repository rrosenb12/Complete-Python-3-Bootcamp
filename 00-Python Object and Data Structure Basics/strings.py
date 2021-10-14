# Character    : h  e  l  l  o
# Index        : 0  1  2  3  4
# Reverse Index: 0 -4 -3 -2 -1

# Slicing (grabbing a subsection of multiple characters)
## [start:stop:step]
### start: index where the slicing will start
### stop: index where the slicing will go up to (AKA, slice does not include this index)
### step: size of "jump" of slice

print(len('hello'))
# 5
# len() returns length of string

mystring = 'Hello World'
mystring[0]
print(mystring[0])

print(mystring[-4])

mystring = 'abcdefghijk'
print(mystring[2:])
# Starting at index 2, print everything to the end

print(mystring[:3])
# Starting at index 0, print everything until index 3, and don't include index 3

print(mystring[3:6])
# Print everything from, and including, index 3, up until, and excluding, index 6

print(mystring[::])
# Print everything from the beginning to the end

print(mystring[::2])
# Print everything from the beginning to the end jumping 2 indexes in between

print(mystring[1:7:2])
# Starting at, and including, index 1, print until, and excluding, index 7, jumping 2 indexes in between

print(mystring[::-1])
# Reverses string (step size of -1)

# You can't change a string (string immutability)

name = "Sam"

# name[0] = 'P' 
## Will error out, you can't assign this a different value
## Strings don't support item assignment

last_letters = name[1:]

# 'am'

pam = 'P' + last_letters
# string concatenation

print(pam)

# You can reassign the whole string to a new value

x = 'Hello World'

x = x + ' it is beautiful outside!'

print(x)
# Hello World it is beautiful outside!

letter = 'z'
letter * 10
# Will return 'z' 10 times in the same string
print(letter*10)

print('2' + '3')
# 23

x.capitalize()
# Capitalizes first letter of x

print(x.upper())
# CAPS LOCK

x.split()
# Splits into an array by white space each letter
## ['Hello', 'World']

x.split('i')
# Will split on the i and remove the i, if there are any
print(x.split('i'))