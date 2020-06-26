import warnings
from libc import printf

# Test the factorial calculation functions.
def factorial_demo():

	# Print factorials of the numbers in the given range.
	for n in range(0, 10):
		printf("%d = %ld\n", n, factorial_iterative(n));
		printf("%d = %ld\n", n, factorial_recursive(n));
		printf("%d = %ld\n", n, factorial_tailcall(n, 1));


# Calculate factorial of the given number. Using recursion.
def factorial_recursive(n):
	if n == 0:
		return 1

	return factorial_recursive(n-1) * n


# Calculate factorial of the given number. Using tail call.
def factorial_tailcall(n, r):
	if (n == 0):
		return r
	r *= n
	return factorial_tailcall(n-1, r)


# Calculate factorial of the given number. Using iterations.
def factorial_iterative(n):
	r = 1
	for i in range(1, n+1):
		r *= i
	return r


def main():

	factorial_demo();

	exit(0);
# end main


if __name__ == "__main__":
	main();
