import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

chosen_word = word_list[random.randint(0, len(word_list) - 1)]
display = []
word_length = len(chosen_word)
lives = 6
print(logo)
print(chosen_word)

for _ in chosen_word:
    display.append("-")
print(display)
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    elif guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    else:
        for position in range(0, word_length):
            if chosen_word[position] == guess:
                display[position] = guess

    if "-" not in display:
        end_of_game = True
        print("You Win The Game")

    print(stages[lives])
    print(display)
