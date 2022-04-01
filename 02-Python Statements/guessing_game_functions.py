import random

answer = random.randint(1,100)
guesses = [0]

def guess():
    player_input = int(input("Pick a number between 1 and 100: "))
    if player_input not in range(1,101):
        print("OUT OF BOUNDS")
        guess()
    else: append_guess(player_input)

def append_guess(player_input):
    guesses.append(player_input)
    print(guesses)
    if guesses[-2]:
        if abs(player_input - answer) < abs(guesses[-2] - answer):
            print("WARMER", guesses)
        else: print("COLDER", guesses)
    else:
        if abs(player_input - answer) <= 10:
            print("WARM")
        else: print("COLD")

while not guesses[-1] == answer:
    guess()
else:
    print("YOU WIN", answer, len(guesses))