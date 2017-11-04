# Create a program that reads a csv file that contains the name of a list of employees, along with their salaries,
# and takes as input an employee's name, and prints that employee's salary.

# Create a dict "salary" that maps employee names to their salaries.

salary = {}

# Open the file using open() and a with: statement. (The salaries.csv file is in the data directory).

# Iterate over the lines of the file.
with open("data/salaries.csv") as file:
    for line in file:
        tokens = line.strip('\n').split(',')
        salary[tokens[0]] = int(tokens[1])

# Split the lines by comma and fill the dict accordingly.

# Input the query.

query = input()

# Ouput the corresponding value from "salary"

print(salary[query])
