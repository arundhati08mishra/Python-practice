'''
Given a list of integers nums, find the largest product of three distinct elements.
The numbers can be negative also.


Appoach:
Sort the numbers. The max product will either be prodcut of last 3 i.e. highest numbers or it can also happen that the negative numbers.
For example:
i/p:	nums = [5, 4, 1, 3, -2, -2]
o/p:	5*4*3 = 60

Or the highest number and 2 negative numbers.
For example:
i/p:	nums = [-10, -2, 1, 4, 10]
o/p:	-10*-2*10 = 200


Therefore, only two cases are possible- either the three largest integers, or the two smallest integers and the largest integer. 
'''
def solve(nums):
    nums.sort()
    mul1 = nums[-1]*nums[-2]*nums[-3]
    mul2 = nums[-1]* nums[1] * nums[0]
    return max(mul1, mul2)
print(solve([-10, -2, 1, 4, 10]))