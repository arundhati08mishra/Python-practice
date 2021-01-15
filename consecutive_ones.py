'''
You are given a list of integers nums which contains at least one 1. Return whether all the 1s appear consecutively.

Ex:
Input:	nums = [1, 1, 0, 1, 1]
Output: False. All 1s do not appear consecutively, there is 0 in between.

Approach:
Using .index() method find the index of first occuring 1 in the list.
Find index of last occuring 1:	 len(nums)-1-nums[::-1].index(1) gives index of last occuring 1.
If in between these two index values, there is a value!=1 then return False.
'''


def solve(nums):
    idx = nums.index(1)
    last_idx = len(nums) -1 - nums[::-1].index(1)

    for i in range(idx,last_idx+1):
        if nums[i]!=1:
            return False

    return True
print(solve([0, 1, 1, 1, 2, 3]))
print(solve([1, 1, 0, 1, 1]))
