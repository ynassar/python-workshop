# Write a program to print all numbers between 0 and 100 that are multiples of 3 or 5.

# The range(start, end) method creates a "list" of numbers between start and end.

# Iterate over the numbers with a For and use an if statement to check each number.

"""
    for(int i = 0; i < 100; i ++){
        if(i % 3 == 0 || i % 5 == 0)
            cout << i << endl;
    }
"""

numbers = range(0,100)

for i in numbers:
    if i % 3 == 0 or i % 5 == 0:
        print(i)