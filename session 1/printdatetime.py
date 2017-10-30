# Python has several built in "modules" (which are "sets" of similar code grouped together). For example, the math module
# contains several math constants and functions.

# The "datetime" module contains a function called datetime.now() that returns the current date and time.
# Write a python program to display the current date and time.

# To be able to reference the code in a module, we must "import" it first.

import datetime

# We can also import specific functions from within the module.


# Get the current date and time by calling the datetime.now() (as datetime.datetime.now() or datetime.now()) function, and store it in a variable.

time = datetime.datetime.now()

# Print the current date and time to the console.

print(time)