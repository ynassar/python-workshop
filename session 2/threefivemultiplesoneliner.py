# Write a one line program to print all numbers between 0 and 100 that are multiples of either 3 or 5.
print([x for x in range(0, 100) if x % 3 == 0 or x % 5 == 0])

# Use a comprehension, then string.join the results.