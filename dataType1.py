print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])

# Write a program that asks the user to input a floating-point number, then converts that input to an integer.
# Print both the original floating-point number and the converted integer.

float_number = float(input("Enter a floating-point number: "))
integer_number = int(float_number)

print(f"The original floating-point number is {float_number}")
print(f"The converted integer is {integer_number}")
print(type(float_number))

# Exercise 2: Sum of Numbers Ask the user to input two numbers, one integer and one floating-point number.
# Then print the sum of these numbers as three different types: as an integer, as a float, and as a string.
# Note that you will need to perform type casting to accomplish this.

integer_number = int(input("Enter an integer: "))
float_number = float(input("Enter a floating-point number:"))
print(f"The sum of the numbers as an integer is {int(integer_number + float_number)}")
print(f"The sum of the number as a float is {float(integer_number + float_number)}")
print(f"The sum of the number as a String is {str(integer_number + float_number)}")
