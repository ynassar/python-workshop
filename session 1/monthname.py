# Write a program to take a month number and print the corresponding month name.

# Create a Python "list" of month names, i.e:
# ['January', 'February', 'March', 'April', etc..]
# and store it in a variable month_names. Then, month_names[0] = 'January', month_names[1] = 'February', etc.

month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Take as input the month number.

month_number = int(input())

# Print the corresponding month_name.

print(month_names[month_number - 1])