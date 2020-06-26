"""
Search for perfect numbers.
.
"""

import math

def isperfect(n):

	d = 2
	sum = 1

	while d <= math.sqrt(n):
		if n % d == 0:
			sum = sum + d + n / d

		d = d + 1

	
	if n == sum:
		return True
	else:
		return False


if __name__ == "__main__":

	print(isperfect(33550336))
	
	nperfects = 0
	print("Searching for perfect numbers...")

	for n in range(2, 10000):
		if isperfect(n):
			nperfects += 1
			print("%d: %d is a perfect number." % (nperfects, n))

		#if n % 1000 == 0:
			#print(n)

