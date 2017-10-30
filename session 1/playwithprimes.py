# Write a python program to print the primes from 0 to 100 in reverse order. The primes from 0 to 100 are as follows:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Create the appropriate Python list.

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Use a For loop to iterate over the primes, but use the [::-1] operator to reverse the list, and print each prime.

for prime in primes[::-1]:
    print(prime)

# Write a python program to print the first 10 primes from 0 to 100.

# Use a For loop to iterate over the primes, using the [:10] operator.

for prime in primes[:10]:
    print(prime)

# Write a python program to print the last 10 primes from 0 to 100.

# Use a For loop to iterate over the primes, using the [:-10] operator.

for prime in primes[:-10]:
    print(prime)

for prime in primes[20:10:-1]