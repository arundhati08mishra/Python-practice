'''
Question: Given a list of integers, return the largest difference of two consecutive integers in the sorted version of the list.

Approach:
Sort the list in decreasing order. So we get consecutive numbers but in decreasing order. Then substract each element at index i with element at index i-1.
And return the max difference. 
'''
def solve(nums):
	nums.sort(reverse=True)
	return max([nums[i]-nums[i+1] for i in range(len(nums)-1)])
print(solve([4, 1, 2, 8, 9, 10]))
print(solve([7, 9, 10]))
