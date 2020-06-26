# Print prime numbers in specified range.

import sys
import math

# Check whether n is a prime number.
def isprime(n):

	if n == 0 or n == 1:
		return False

	# 2 is a special case.
	if n == 2:
		return True

	# Do not check the even numbers (they are never prime exept for 2).
	if n % 2 == 0:
		return False

	# Try to divide the number by other odd numbers.
	for d in range(3, int(math.sqrt(n))+1, 2):

		# If the number can be divided without a remainder, it is not prime.
		if n % d == 0:
			return False
	
	return True
# isprime


# Print and count prime numbers in a specified range.
def print_prime_numbers(upper):

	nprimes = 0

	for n in range(0, upper):
		if isprime(n):
			nprimes += 1
			print(n)

	print("%d prime numbers have been found." % nprimes)
# prime_number_demo


if __name__ == "__main__":

	argc = len(sys.argv) 
	if argc < 2 or argc > 3:
		print("Usage:\n\tprime n\n\tprime -p UPPER")
		sys.exit(1)


	if argc == 2:
		try:
			n = int(sys.argv[1])
		except(ValueError):
			print("Wrong type of argument")
			sys.exit(1)

		if isprime(n):
			print("%d is a prime number" % n)
			sys.exit(0)
		else:
			print("%d is not a prime number" % n)
			sys.exit(1)

	# Print numbers in the range.
	arg = sys.argv[1]
	if arg[0] == '-' and arg[1] == 'p':
		n = int(sys.argv[2])
		print_prime_numbers(n)
	
