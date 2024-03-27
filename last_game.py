from game_data import data
from guess_art import vs
from guess_art import logo
import random

all_data = data


def get_two_value(local_data):
    compare_a = random.choice(local_data)
    compare_b = random.choice(local_data)
    return [compare_a, compare_b]


def show_information(instgram_list):
    print(f"Compare A :{instgram_list[0]['name']}, {instgram_list[0]['description']}, {instgram_list[0]['country']}")
    print(vs)
    print(f"Against B :{instgram_list[1]['name']}, {instgram_list[1]['description']}, {instgram_list[1]['country']}")


def check_answer(instgram_list, answer):
    if answer == "A":
        if instgram_list[0]['follower_count'] > instgram_list[1]['follower_count']:
            return True
        else:
            return False
    elif answer == "A":
        if instgram_list[1]['follower_count'] > instgram_list[0]['follower_count']:
            return True
        else:
            return False


def game():
    score = 0
    is_correct_answer = True
    while is_correct_answer:
        print(logo)
        new_list = get_two_value(all_data)
        show_information(new_list)
        answer = input("Who has more followers ? Type A or B ? \n")
        is_correct_answer = check_answer(new_list, answer)
        if is_correct_answer:
            score += 1
        print(f"Your Score is {score}")


game()
