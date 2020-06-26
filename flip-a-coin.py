from random import random

heads = 0
tails = 0

for i in range(100):
	n = int(random() * 2)
	if n == 0:
		heads += 1
	else:
		tails += 1

print("Heads: %d; tails: %d\n" % (heads, tails))
