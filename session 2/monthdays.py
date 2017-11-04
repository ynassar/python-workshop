# Write a program to take the name of a month and print the number of days in it.
# The number of days per month are as follows:




# Create a python "dict" num_days the maps the name of the month to the # of days. i.e. num_days['January'] = 31, etc..

num_days = { 'January' : 31,
    'February' : 28,
    'March' : 31,
    'April' : 30,
    'May' : 31,
    'June' : 30,
    'July' : 31,
    'August' : 31,
    'September' : 30,
    'October' : 31,
    'November' : 30,
    'December' : 31
    }

# Input the name of the month from the user.

month_name = input()

# Print the corresponding num_days.

print(num_days[month_name])