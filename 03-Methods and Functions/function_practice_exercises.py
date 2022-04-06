# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd

from doctest import master


def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return max(a,b)
    else:
        return min(a,b)

lesser_of_two_evens(2,4)
lesser_of_two_evens(2,5)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(string=''):
    firstLetter = string.split()[0][0].lower()
    secondLetter = string.split()[1][0].lower()
    return firstLetter == secondLetter

animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False

def makes_twenty(a,b):
    return (a+b) == 20 or a == 20 or b == 20

makes_twenty(20,10)
makes_twenty(12,8)
makes_twenty(2,3)

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    newName = ''
    for idx in range(len(name)):
        if idx == 0 or idx == 3:
            newName = newName + name[idx].upper()
        else: newName = newName + name[idx]
    return(newName)

old_macdonald('macdonald')

# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(sentence):
    newSentence = sentence.split()
    return(" ".join(newSentence[::-1]))

master_yoda("I am home")
master_yoda("We are ready")

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    if abs(n - 100) < 10 or abs(n-200) < 10:
        return(True)
    else:
        return(False)

almost_there(104)
almost_there(150)
almost_there(209)

# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def find_33(my_list):
    for index,number in enumerate(my_list):
        print(index,number)
        

find_33([1,3,3])