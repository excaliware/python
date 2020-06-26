import warnings

# The fibonacci numbers.
def fibonacci_demo():

	n = 10;

	print("The %d-th fibonacci number is %d" % (n, fibonacci(n)));
	print("The %d-th fibonacci number is %d" % (n, fibonacci_iter(n)));
#

# Calculate the n-th element of the fibonacci series.
# Using recursion -- O(2**n) -- very inefficient.
def fibonacci(n):
	if n == 1 or n == 0:
		return n

	return fibonacci(n-2) + fibonacci(n-1)
#

# Calculate the n-th element of the fibonacci series.
# Using iteration.
def fibonacci_iter(n):
	n1 = 0
	n2 = 1
	print(0, n1)
	print(1, n2)

	for i in range(2, n+1):
		t = n1
		n1 = n2
		n2 = t + n2
		print(i, n2)

	return n2
#

def main():

	fibonacci_demo()

	exit(0)
#


if __name__ == "__main__":
	main()
