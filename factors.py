"""
Find prime factors of a given number.

"""

import math
import sys

"""
Find and print the prime factors of n.
"""
def print_factors(n):

	sys.stdout.write("%d: " % n)

	# First, find the factor 2, if any.
	while n % 2 == 0:
		sys.stdout.write("%d " % 2)
		n //= 2


	# From now on, check odd numbers only.
	d = 3
	while d <= math.sqrt(n):

		while n % d == 0:
			# Divide by this factor while it is possible.
			n //= d
			sys.stdout.write("%d " % d)
		
		d += 2

	
	if n > 1:
		sys.stdout.write("%d " % n)

	sys.stdout.write('\n')


if __name__ == "__main__":

	for n in range(1, 1025):
		print_factors(n)

	print_factors(100000003253453470)

