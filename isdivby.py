# This program checks whether the given number can be divided by numbers 
# from 2 to 12. The modulus operator has not been used at all.

import sys

def main():

	# Array of pointers to the functions.
	isdivby = [None, None, isdivby2, isdivby3, isdivby4, isdivby5, isdivby6, isdivby7, isdivby8, isdivby9, isdivby10, isdivby11, isdivby12]
	show_demo(isdivby)
	if len(sys.argv) == 3:
		num = int(sys.argv[1])
		div = int(sys.argv[2])

	elif len(sys.argv) == 2 and sys.argv[1] == "-":
		num = int(input("Enter a number: "))
		div = int(input("Enter a divisor: "))

	elif len(sys.argv) == 2 and sys.argv[1] == "demo":
		show_demo(isdivby)
		exit(0)

	else:
		print("Usage: isdivby NUMBER DIVISOR")
		print("   Or: isdivby -")
		print("   Or: isdivby demo")
		exit(1)
		
	if isdivby[div](num):
		result = ""
	else:
		result = " not"

	print("\n{0} is{1} divisible by {2}".format(num, result, div))

	exit(0)
# end main


# Print demo chart demonstrating division of the numbers from 2 to 24.
def show_demo(isdivby):

	print("/  ", end='')

	# Print the header of the table (divisors).
	for d in range(2, 13):
		print(" {0}  ".format(d), end='')

	print()

	# Sample numbers to divide.
	for n in range(2, 25):
		print("{0:2}  ".format(n), end='')

		for i in range(2, 13):
			if isdivby[i](n):
				print(" +  ", end='')
			else:
				print(" -  ", end='')
		
		print()

# end show_demo


# The number can be divided by 2
# if it is even, i.e., its last number is 0, 2, 4, 6 or 8.
def isdivby2(n):

	if n - n // 10 * 10 in (0, 2, 4, 6, 8):
		return True
	else:
		return False

#

# The number can be divided by 3
# if the sum of its digits can be divided by 3.
def isdivby3(n):

	sum_digits = 0
	
	while n / 10:
		digit = n - n // 10 * 10
		sum_digits = sum_digits + digit

		# Discard the last digit
		n = n // 10
	
	# Add the rest of the number (last digit).
	sum_digits = sum_digits + n
	
	if sum_digits // 3 * 3 == sum_digits:
		return True
	else:
		return False

# end isdivby3

# The number can be divided by 4
# if its last two digits are zeros or make a number divisible by 4.
def isdivby4(n):

	digits = n - n // 100 * 100
	if digits // 4 * 4 == digits:
		return True
	elif digits == 0:
		return True
	else:
		return False

# end isdivby4

# The number can be divided by 5
# if its last number is 0 or 5.
def isdivby5(n):

	if n - n // 10 * 10 in (0, 5):
		return True
	else:
		return False

# end isdivby5

# The number can be divided by 6
# if it is divisible by both 2 and 3.
def isdivby6(n):

	if isdivby2(n) and isdivby3(n):
		return True
	else:
		return False

# end isdivby6

# The number can be divided by 7
# (Not implemented yet).
def isdivby7(n):

	if n // 7 * 7 == n:
		return True
	else:
		return False

# end isdivby7

# The number can be divided by 8
# if its three last digits are zeros or make a number divisible by 8.
def isdivby8(n):

	digits = n - n // 1000 * 1000
	if digits // 8 * 8 == digits:
		return True
	elif digits == 0:
		return True
	else:
		return False

# end isdivby8

# The number can be divided by 9
# if the sum of its digits can be divided by 9.
def isdivby9(n):

	sum_digits = 0
	
	while n / 10:
		# Add the last digit to the sum.
		digit = n - n // 10 * 10
		sum_digits = sum_digits + digit

		# Discard the last digit
		n = n // 10
	
	# Add what is left.
	sum_digits = sum_digits + n
	
	if sum_digits // 9 * 9 == sum_digits:
		return True
	else:
		return False

# end isdivby9

# The number can be divided by 10
# if its last digit is 0.
def isdivby10(n):

	if n - n // 10 * 10 == 0:
		return True
	else:
		return False

# end isdivby10

# The number can be divided by 11
# if the subtraction of the sum of the odd digits and the sum of the even 
# digits is zero or divisible by 11.
def isdivby11(n):

	isodd = True
	odd_digits = even_digits = 0

	while n / 10:
		if isodd:
			odd_digits = odd_digits + n - n // 10 * 10
			isodd = False
		else:
			even_digits = even_digits + n - n // 10 * 10
			isodd = True

		n = n // 10
		
	sub = odd_digits - even_digits

	if sub // 11 * 11 == sub:
		return True
	elif sub == 0:
		return True
	else:
		return False

# end isdivby11

# The number can be divided by 12
# if it is divisible by both 3 and 4.
def isdivby12(n):

	if isdivby3(n) and isdivby4(n):
		return True
	else:
		return False

# end isdivby12


if __name__ == "__main__":
	main()

