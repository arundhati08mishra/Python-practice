'''
Given a list of integers nums, return the largest integer k where k and -k both exist in nums
If there's no such integer, return -1.

Example:
Input = [-4, 1, 8, -5, 4, -8]
Output = 8

Approach: 
Use a set to get the unique values. Loop throught the set and for every i in the set, map i to its additive inverse in a dictionary.
For every i whose -i exists in nums, return the max i.

 '''

def solve(nums):
	maxx = -1
	set1 = set(nums)
	dict1 = {}

	for i in set1:
		dict1[i] = -i
		if dict1[i] in set1 and i>maxx:
			maxx = i

	return maxx

print(solve([5, 6, 1, -2]))
print(solve([1, 2, 0, 3, 4]))