"""
Convert temprature from Celsius to Fahrenheit or vice versa.

"""
import sys

def main():

	if len(sys.argv) == 3:
		mode = str(sys.argv[1])
		value = int(sys.argv[2])

	else:
		print_usage()
		exit(-1)
		

	if mode == 'f':
		print("%.1f" % f2c(value))

	elif mode == 'c':
		print("%.1f" % c2f(value))

	else:
		print_usage()
		exit(-1)


def print_usage():
	print("Usage: temperature {f|c} VALUE")


def f2c(f):
	return (f - 32) / 1.8	# 9 / 5

def c2f(c):
	return c * 1.8 + 32


if __name__ == "__main__":

	main()
