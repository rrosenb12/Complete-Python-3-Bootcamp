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
    """ newName = ''
        for idx in range(len(name)):
          if idx == 0 or idx == 3:
            newName = newName + name[idx].upper()
          else: newName = newName + name[idx]
        return(newName) """
    if len(name) < 5:
        return("Too Short")
    else:
        first_half = name[:3]
        second_half = name[3:]
        return(first_half.capitalize() + second_half.capitalize())

old_macdonald('coen')
old_macdonald('macdonald')

# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(sentence):
    newSentence = sentence.split()
    return(" ".join(newSentence[::-1]))

master_yoda("I am home")
master_yoda("We are ready")

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    return (abs(n - 100) < 10) or (abs(n-200) < 10)

almost_there(104)
almost_there(150)
almost_there(209)

# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def find_33(my_list):
    for i in range(0, len(my_list) - 1):
        # if my_list[i:i+2] == [3,3]
        if my_list[i] == 3 and my_list[i + 1] == 3:
            return(True)
    return(False)
        

find_33([1,3,3])
find_33([1, 3, 1, 3])

#### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(string):
    new_string = ''
    for letter in string:
        new_string += letter*3
    return(new_string)

paper_doll("hello")

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# this problem has bad instructions lol

def blackjack(a,b,c):
    if (a + b + c) <= 21:
        return("sum:", a+b+c)
    elif (a + b + c) - 10 <= 21 and (a == 11 or b == 11 or c == 11):
        return("total sum minus 10:", ( a + b + c ) - 10)
    else:
        return("BUST")

blackjack(5,6,7)
blackjack(9,9,9)
blackjack(9,9,11)

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(list):
    new_list = []
    add = True
    for number in list:
        while add:
            if number !=6:
                new_list.append(number)
                break
            else: add = False
        while not add:
            if number !=9:
                break
            else:
                add = True     
    return(sum(new_list))
 
summer_69([])
summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11])