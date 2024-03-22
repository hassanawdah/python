import random
import string

print("Welcome to the PyPassword Generator!")

# Get user input for the number of each character type
nr_letters_small = int(input("How many small letters would you like in your password?\n"))
nr_letters_capital = int(input("How many capital letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
total_length = int(input("What's the total length of the password?\n"))

# Ensure total password length is at least equal to the sum of requested character types
min_length = nr_letters_small + nr_letters_capital + nr_symbols + nr_numbers
if total_length < min_length:
    print(f"Total length is set to minimum required length: {min_length}")
    total_length = min_length

# Initialize list for password characters
password_list = []


# Helper function to add characters of a specific type to the password list
def add_characters(char_list, count):
    for _ in range(count):
        password_list.append(random.choice(char_list))


# Add characters to the password list
add_characters(string.ascii_lowercase, nr_letters_small)
add_characters(string.ascii_uppercase, nr_letters_capital)
add_characters(string.punctuation, nr_symbols)
add_characters(string.digits, nr_numbers)

# If the total length is greater than the sum, add random characters until the length is met
additional_chars_needed = total_length - len(password_list)
if additional_chars_needed > 0:
    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    add_characters(all_chars, additional_chars_needed)

# Shuffle the list to randomize character order and convert to string
random.shuffle(password_list)
password = ''.join(password_list)

# Output the generated password
print(f"Your generated password is: {password}")
