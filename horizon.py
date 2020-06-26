import sys
import math

# Calculate the distance to the horizon.

if len(sys.argv) != 2:
	sys.stderr.write("Usage: horizon HEIGHT\n");
	exit(1)


r = 6_378_000
h = float(sys.argv[1])

d = math.sqrt(2 * r * h + h ** 2)

print(d)
