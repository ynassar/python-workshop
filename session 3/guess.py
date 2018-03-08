# Our task here is to write a python program to take a filename representing an episode and print the expected title of the series,
# the episode number and the season number.

# For this task, we use the guessit library from the PyPI
# The PyPI, or Python Package Index is a group of "python" packages installable using a simple command line tool named pip.

# To install the guessit module from pip, we open a terminal and run "pip install guessit". The module is now installed on python.

# We then import the module.
from guessit import guessit
# guessit has a method called guessit() that returns the episode number, season number, and expected title.
print(guessit.guessit('hi'))