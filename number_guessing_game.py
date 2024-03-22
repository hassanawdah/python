# Create a simple number guessing game:
import random
from itertools import count

# Use the random module to generate a random number between 1 and 100.
# Ask the user to guess the number.
# Each time the user guesses, tell them if their guess is too high or too low.
# Once the user guesses the correct number, congratulate them and print the number of tries it took them.


guessNumbers = random.randint(1, 100)
count_value = 0
for number in count(0):
    userInput = int(input("Please select number\n "))
    count_value = count_value + 1
    if userInput == guessNumbers:
        print(f"congratulate you get in {count_value} time")
        break
    elif userInput > guessNumbers:
        print("too high ")
    else:
        print("Too Low ")
