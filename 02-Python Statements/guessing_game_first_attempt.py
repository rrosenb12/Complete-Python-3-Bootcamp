import random

answer = random.randint(1,100)
guess = 0
guesses = 0
difference = 0

while guess != answer:
    while not guesses:
        player_guess = int(input("Pick a number between 1 and 100: "))
        if player_guess not in range(1,101):
            print("OUT OF BOUNDS")
            pass
        else:
            guess = player_guess
            guesses = []
            guesses.append(guess)
            difference = guess - answer
            if len(guesses) == 1:
                if guess == answer:
                    print("YOU WIN")
                elif abs(difference) <= 10:
                    print("WARM, guesses:", guesses, "difference:", difference)
                else:
                    print("COLD, guesses:", guesses, "difference:", difference)
                    
    while guesses and guess != answer:
        player_guess = int(input("Pick a number between 1 and 100: "))
        guess = player_guess
        guesses.append(guess)
        if guess == answer:
            print("YOU WIN. ATTEMPTS:", len(guesses))
        elif abs(guesses[-1] - guesses[-2]) <= abs(difference):
            difference = guess - answer
            print("WARMER, guesses:", guesses, "difference:", difference)
        else:
            difference = guess - answer
            print("COLDER, guesses:", guesses, "difference:", difference)

