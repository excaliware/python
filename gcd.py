"""
Find the highest common factor (HCF) or the greatest common divisor (GCD) of the given numbers.

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
		# Divide by this factor while it is possible.
		while n % d == 0:
			n = n // d
			factors.append(d)
	
		d = d + 2
	
	if n > 1:
		factors.append(n)

	return factors


"""
Find the highest common factor (HCF) or the greatest common divisor (GCD) of the given numbers.
"""
def calc_gcd(nums):

	ndict = {}
	result = {}

	for n in nums:

		ndict[n] = {}

		factors = find_factors(n)

		for f in factors:
		
			if ndict[n].get(f) == None:
				ndict[n][f] = 1
			else:
				ndict[n][f] += 1

	for f in ndict[nums[0]].keys():
		result[f] = ndict[nums[0]][f]

	for n in nums[1:]:
		for f in ndict[n].keys():
			if result.get(f) == None:
				continue
			elif ndict[n][f] < result[f]:
				result[f] = ndict[n][f]

	for n in nums[1:]:
		for f in list(result.keys()):
			if ndict[n].get(f) == None:
				if f in nums:
					return 1
				del result[f]

	p = 1
	for f in result.keys():
		p *= math.pow(f, result[f])

	return int(p)


# Euclid's algorithm
def gcd_euclid(a, b):
    while (b != 0):
        r = a % b
        a = b
        b = r

    return a


if __name__ == "__main__":

	nums = [9, 18, 27]
	
	gcd = calc_gcd(nums)
	
	print("The HCF (GCD) of %s is %d" % (nums, gcd))

	# Check the correctness of the result.
	for n in nums:
		if n % gcd != 0:
			print("%d / %d = %d" % (n, gcd, n / gcd))

