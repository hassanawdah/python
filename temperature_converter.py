# Create a program that converts temperatures from Celsius to Fahrenheit. The user should input
# the temperature in Celsius as a string, and the program should convert this to both an integer and a floating-point
# number in Fahrenheit. Use the formula: Fahrenheit = (Celsius * 9/5) + 32. Print both the integer and floating-point
# result with appropriate messages.
celsius = float(input("Enter The Temperature in Celsius:"))
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit as an integer is {int(fahrenheit)}")
print(f"The temperature in Fahrenheit as a float is {float(fahrenheit)}")

combined_names = "name1" + "name1"
lower_name = combined_names.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
count_of_true_Letters = t+r+u+e


l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

count_of_love_Letters = l +o + v + e

score = str(count_of_true_Letters) + str(count_of_love_Letters)
score = int(score)
if(score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >=40) and (score <=50):
  print(f"Your score is {score}, you are together")
else:
 print(f"Your score is {score}.")