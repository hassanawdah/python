import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0, len(word_list) - 1)]
display = []
word_length = len(chosen_word)
print(chosen_word)


for _ in chosen_word:
    display.append("-")
print(display)
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter").lower()
    for position in range(0, word_length):
        if chosen_word[position] == guess and display[position] == "-":
            print(position)
            display[position] = guess

    print(display)
    if "-" not in display:
        end_of_game = True
        print("You Win The Game")

print(display)
