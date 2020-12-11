'''
Given a list of integers nums and an integer k, return true if you can remove exactly one element from the list to make the average equal to exactly k.

Example:
nums = [1, 2, 3, 10]
k = 2

Output: True
We can take 10 out to reach an average of 2 since (1 + 2 + 3) / 3 = 2
'''
def solve(nums, k):
	for i in range(len(nums)):
		if( (sum(nums)-nums[i])/(len(nums)-1)) == k: # substract ith element from sum of elements and then divide by len(nums)-1 i.e. 3 here to get average. Check if that = k. If not, continue with next element. If k is obtained, return True. If the loop has gone over all elements and k is not otained, return False. 
			return True
	return False
print(solve([1, 2, 3, 10], 2))
print(solve([1, 2, 3, 10], 5))
print(solve([1, 2, 3, 10], 10))