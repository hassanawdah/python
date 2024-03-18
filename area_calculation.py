# Write a program that calculates the area of a circle. Ask the user to input the radius as a string,
# convert this radius to a floating-point number, and then use it to calculate the area.
# Assume pi is 3.14159. Print the result as a float with a message.
PI = 3.14159

radius = float(input("Enter the radius of the circle:"))
area = PI * radius ** 2
print(f"The area of the circle is {area:.2f} or {round(area,2)}")
