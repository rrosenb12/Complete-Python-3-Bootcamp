# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
myString = st.split()
for x in myString:
    if x[0].lower() == 's':
        print(x)

# Use range() to print all the even numbers from 0 to 10.

for num in range(0,11):
    if num%2==0:
        print(num)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

myRange = range(1,51)
rangeByThree = [num for num in myRange if num%3==0]
print(rangeByThree)

# Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2==0:
        print(word,"even")

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

fizzBuzz = range(1,100)
for num in fizzBuzz:
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)

# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
firstLetters = [x[0] for x in st.split()]
print(firstLetters)