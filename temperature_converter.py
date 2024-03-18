# Create a program that converts temperatures from Celsius to Fahrenheit. The user should input
# the temperature in Celsius as a string, and the program should convert this to both an integer and a floating-point
# number in Fahrenheit. Use the formula: Fahrenheit = (Celsius * 9/5) + 32. Print both the integer and floating-point
# result with appropriate messages.
celsius = float(input("Enter The Temperature in Celsius:"))
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit as an integer is {int(fahrenheit)}")
print(f"The temperature in Fahrenheit as a float is {float(fahrenheit)}")

