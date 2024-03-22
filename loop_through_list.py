# Create a program to find and print the first, third, and fifth elements of a given list using a loop. If the list
# has fewer than five elements, print an error message.


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if len(my_list) < 5:
    print("The length of the list is fewer than five ")
else:
    for number in range(1, 6, 2):
        print(number)
