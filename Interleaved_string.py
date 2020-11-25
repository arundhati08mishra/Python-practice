'''
From BinarySearch
Given two strings s0 and s1, return the two strings interleaved, starting with s0. 
If there are leftover characters in a string they should be added to the end.
Example 1:
Input:

s0 = "abc"
s1 = "xyz"
Output:

"axbycz"

Example 2
Input:

s0 = "abc"
s1 = "x"
Output:

"axbc"

'''
def solve(s0, s1): #takes two strings
	s3=''  #empty string
	i=0
	while i<len(s0) and i<len(s1):
		s3=s3+(s0[i]) #first ith value of s0
		s3=s3+(s1[i]) #followed by ith value of s1
		i+=1
	s3=s3+(s0[i:]) #if any leftover characters are there
	s3=s3+(s1[i:])
	return s3
print(solve('abc', 'x'))