# Write a python program to delete all .txt files from the data directory.

# Import the os module to be able to access os commands.
import os
# Use the os.listdir() function to get a list of all files in the directory.
files = os.listdir('data')

# Iterate over the files.

for file in files:
    if file.endswith('.txt'):
        os.remove(os.path.join('data', file))

# Check if the file ends with .txt, if so, use the os.remove command to remove it. 
# Use os.path.join() to get the path of the file inside the directory.
