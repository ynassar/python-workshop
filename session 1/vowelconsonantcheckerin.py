# Write a program to check whether a given letter is a vowel or a consonant.

# Create a Python "list" of vowels.

vowels = ['a','e','i','o','u']
# Take the letter as input().

letter = input()

# Use the Python "in" to check whether the letter is in the list of vowels.

if letter in vowels:
    print("That's a vowel.")
else:
    print("That's a consonant.")