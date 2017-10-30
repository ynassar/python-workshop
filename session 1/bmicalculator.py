# Compute the body mass index of the user, taking as input their height and weight.
# BMI is computed as weight over height squared, and is rounded to 2 decimal places.

# To input a value from the user we use input() (but this gives us a string!).
# Assign the inputted value of height, and weight to variables.

height = float(input("Please input your height."))
weight = float(input("Please enter your weight."))

# Compute the BMI. In python, a^x is written as a**x.

bmi = weight / (height ** 2)

# Output the answer rounded to 2 decimal places.

print(round(bmi, 2))