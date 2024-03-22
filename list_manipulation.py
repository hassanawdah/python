# Creates a list of numbers from 1 to 10.
# Appends the next number (11) to the end of the list.
# Inserts the number 0 at the beginning of the list.
# Slices the list to only include numbers from 2 to 8.
# Reverses the sliced list.
# Prints the final list.

numbers = list(range(1, 11))
numbers.append(11)
numbers.insert(0, 0)
sub_numbers = numbers[2:8]
sub_numbers.reverse()
print(sub_numbers)
