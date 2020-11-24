'''
From LeetCode.
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example 1:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 2:
Input: nums = [3,3], target = 6
Output: [0,1]
'''
def twoSum(nums, target):
	for i in range(len(nums)):
		j=target-nums[i] 
		if j in nums and nums.index(j)!=i: 
			return ([i, nums.index(j)])

print(twoSum([3,2,4], 6))