# Write a python program to reverse a sentence taken as input from the user.

# i.e "Hi I'm Yousef" -> "Yousef I'm Hi"

# Input the sentence as a string.

line = input("Enter a sentence to reverse.")

# Use the string.split() method to convert the string to a list.

sentence_tokens = line.split(' ')

# Reverse the list.

rev = sentence_tokens[::-1]

# Use the string.join method to convert the list back into a space-separated string.

reversed_sentence = ' '.join(rev)

# Print the string.

print(reversed_sentence)