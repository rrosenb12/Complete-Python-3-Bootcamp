import random

# Set an answer and set the first guess to 0. 0 is an invalid guess, and guesses[0] returns False
answer = random.randint(1,100)
guesses = [0]

# While the most recent guess is not the answer
while guesses[-1] != answer:
    # Ask for a number
    guess = int(input("Pick a number between 1 and 100: "))
    # If the input is not between 1 - 100, inclusive, ask for another number and continue this cycle
    if guess not in range(1,101):
        print("OUT OF BOUNDS")  
        continue      

    # Add the valid guess to the list    
    guesses.append(guess)
    
    # If the guess is the answer, they win. Break the cycle
    if guess == answer:
        print(f"YOU WIN. THE NUMBER WAS {guess}. ATTEMPTS: {len(guesses)}")
        break
            
    # If there are at least 2 valid guesses, calculate the difference.         
    if guesses[-2]:
        # If the absolute difference between this guess and the answer is less than the difference of the previous guess, tell the user they are warmer
        if abs(guess - answer) < abs(guesses[-2] - answer):
            print("WARMER, guesses:", guesses)
        else:
            print("COLDER, guesses:", guesses)
    # If there are not two valid guesses, take the absolute difference of the answer and the guess
    else:
        # If the difference is less than or equal to 10, tell them they are close.
        if abs(answer - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')