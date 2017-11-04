# Write a python function to get the number of spaces, commas, and letter a's in a string.

# Create a function using the def: signature.

def get_counts(input_str):
    num_spaces = 0
    num_commas = 0
    num_as = 0
    for char in input_str:
        if char == ' ':
            num_spaces += 1
        elif char == ',':
            num_commas += 1
        elif char == 'a':
            num_as += 1
    return num_spaces, num_commas, num_as

# Iterate over the string and increment the corresponding counts.

# Return the counts.

input_str = input()
num_spaces, num_commas, num_as = get_counts(input_str)