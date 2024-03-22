# Generate a random number using random.randint. Ask the user to guess whether the number is odd or even.
# Display a message indicating whether the user guessed correctly or not.

import random

guess_number = random.randint(0, 1000)
print("Guess the number")
user_guess = int(input("Type 0 for even or 1 for odd\n"))
if user_guess == 0 and guess_number % 2 == 0:
    print(f"Computer guess is {guess_number} and you win")
elif user_guess == 1 and guess_number % 2 == 1:
    print(f"Computer guess is {guess_number} and you win")
else:
    print(f"Computer guess is {guess_number} and you lose")
