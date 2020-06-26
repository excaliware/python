"""
Find the lowest common multiple (LCM) of the given numbers.

"""

import math

"""
Find the prime factors of the given number.
"""
def find_factors(n):

	factors = []

	# First, find the factor 2, if any.
	while n % 2 == 0:
		n = n // 2
		factors.append(2)

	# From now on, check odd numbers only.
	d = 3
	while d <= math.sqrt(n):

		# Divide by the factor while it is possible.
		while n % d == 0:
			n = n // d
			factors.append(d)
		
		d = d + 2

	if n > 1:
		 factors.append(n)

	return factors


"""
Find the lowest common multiple (LCM) of the given numbers.
"""
def calc_lcm(nums):

	ndict = {}
	result = {}
	
	for n in nums:
		for f in find_factors(n):

			if ndict.get(f) == None:
				ndict[f] = 1
			else:
				ndict[f] += 1

		for f in ndict.keys():
			if result.get(f) == None:
				result[f] = ndict[f]
			elif ndict[f] > result[f]:
				result[f] = ndict[f]

		# New dict for the next number, if any.
		ndict = {}

	p = 1
	for f in result.keys():
		p *= math.pow(f, result[f])

	return int(p)

# An alternative approach.
def lcm(a, b):
    return a * b / gcd(a, b)


if __name__ == "__main__":

	nums = [12, 18, 5, 3, 10]
	
	lcm = calc_lcm(nums)

	print("The LCM of %s is %d" % (nums, lcm))

	# Check the correctness of the result.
	for n in nums:
		if lcm % n != 0:
			print("%d / %d = %d" % (lcm, n, lcm / n))

