# Using the os and datetime modules, make a running clock with millisecond accuracy.

# import the modules

import datetime
import os

# create an infinite loop (we don't want our clock to stop!) using a while 1:

while True:
    os.system("cls")
    print(datetime.datetime.now())

# clear the terminal using os.system('clear') or os.system('cls') 
# print the current time