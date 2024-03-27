import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(cards_):
    if sum(cards_) == 21 and len(cards_) == 2:
        return 0
    if 11 in cards_ and sum(cards_) > 21:
        cards_.remove(11)
        cards_.append(1)
    return sum(cards_)


# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
def deal_card(cards_):
    return random.choice(cards_)


# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
is_game_over = False
user_score = 0
computer_score = 0
for i in range(2):
    user_cards.append(deal_card(cards))
    computer_cards.append(deal_card(cards))

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"Your cards: {user_cards} current score:  user_score")
print(f"Computer's first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.


# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
