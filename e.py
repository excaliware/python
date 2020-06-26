from random import random

def main():
	print("e = %.16f\n" % calc_e())
	print("Average number of choices: %f" % sum_randoms_simulation())


# Test sum_randoms; it should converge to e (2.718281828)
def sum_randoms_simulation():
    sum = 0
    num_trials = 1000000
    for i in range(num_trials):
        sum += sum_randoms()

    return float(sum) / num_trials


# Sum random numbers until the sum exceeds 1.0. Return the number of choices.
def sum_randoms():
    sum = 0.0
    n = 0
    while sum <= 1.0:
       x = random() 
       sum += x
       n += 1

    return n


# Calculate the number e up to a specified precision.
def calc_e():

	PRECISION = 0.000000001
	e = 1
	n = 1
	prev = 0

	while (e - prev) > PRECISION:
		prev = e
		e += 1.0 / factorial(n)
		print("n = %d; e = %f\t" % (n, e)),
		n += 1

	return e


# Calculate factorial of a given number.
def factorial(n):
	r = 1
	for i in range(1, n+1):
		r *= i
	return r


if __name__ == "__main__":
	main()
