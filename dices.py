# Histogram of multiple throws of dices.

from random import random

results = [0] * 13

for i in range(1000):
	
	n1 = int(random() * 6) + 1
	n2 = int(random() * 6) + 1
	sum = n1 + n2
	print("%d + %d = %d" % (n1, n2, sum))

	results[sum] += 1

for i in range(2, 13):
	print("%2d: %d" % (i, results[i])),

