# Find all pairs of the numbers the sum of which is equal to the given number.

import warnings

nums = [1, 3, 4, 6, 7, 9, 11, 14, 16, 19]

# Given number
k = 20

# Left/right indexes
l = 0
r = len(nums) - 1

# First, discard too big numbers.
while nums[l] + nums[r] > k:
	r -= 1

while nums[l] + nums[l+1] <= k:
	while nums[l] + nums[r] > k:
		r -= 1

	if nums[l] + nums[r] == k:
		print(nums[l], nums[r])

	l += 1
	r = len(nums) - 1

