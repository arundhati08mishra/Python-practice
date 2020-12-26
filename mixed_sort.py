'''
Question: 

Given a list of integers nums, sort the array such that:
-> All even numbers are sorted in increasing order
-> All odd numbers are sorted in decreasing order
-> The relative positions of the even and odd numbers remain the same.

Input:
nums = [8, 13, 11, 90, -5, 4]
Output:
[4, 13, 11, 8, -5, 90]
Explanation: The even numbers are sorted in increasing order, the odd numbers are sorted in decreasing number, and the relative positions were [even, odd, odd, even, odd, even] and remain the same after sorting.

Approach:
Create separate lists for even numbers and odd numbers. Odd numbers have to be added in decreasing number and even increasing, we sort them in opposite order i.e.
sort the even list in decreasing order and odd list in increasing. We then add the elements in the orignal array by using pop(). 
This will ensure even numbers are added increasingly and odd numbers are added decreasingly.   

'''
def solve(nums):
	even_nums = []
	odd_nums = []

	for i in nums:
		if i%2==0:
			even_nums.append(i)
		else:
			odd_nums.append(i)
	even_nums.sort(reverse=True)
	odd_nums.sort()

	for i in range(len(nums)):
		if nums[i]%2==0:
			nums[i]= even_nums.pop()
		else:
			nums[i]= odd_nums.pop()
	return nums
print(solve([8, 13, 11, 90, -5, 4]))