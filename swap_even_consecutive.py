'''
Question: Given an integer list nums, swap every consecutive even integer with each other.
For ex:nums = [2, 3, 4, 6, 8]
o/p: [4, 3, 2, 8, 6]
2 and 4 got swapped and then 6 and 8 got swapped. 3 being odd wasn't swapped.

Approach:
Once a pair is swapped, we don't want to swap them again i.e. when 2 and 4 get swapped, 2 and 6 shouldn't be swapped.
For this we maintain a variable: prev = -1 indicating no previous even number to be swapped. 
If there is an even number available for swap then we store the index of that number in prev.

'''

def solve(nums):
	prev = -1
	for i in range(len(nums)):
		if nums[i]%2 == 0:
			if prev >= 0:
				nums[i], nums[prev] = nums[prev], nums[i]
				prev = -1
			else:
				prev = i
	return nums
print(solve([2, 3, 4, 6, 8]))
print(solve([2, 3, 4, 6]))