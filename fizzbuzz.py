"""
This program prints the numbers from 1 to 100. For multiples of three, print 'Fizz' instead of the number and for multiples of five print 'Buzz'. For numbers which are multiples of both three and five, print 'FizzBuzz'.
"""

for i in range(1, 101):

	mult3 = i % 3 == 0
	mult5 = i % 5 == 0

	if mult3 and mult5:
		print("FizzBuzz", end=' ')
		continue

	if mult3:
		print("Fizz", end=' ')
		continue

	if mult5:
		print("Buzz", end=' ')
		continue

	print(i, end=' ')

