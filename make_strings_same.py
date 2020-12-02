'''
Question: MAKE STRINGS SAME (from BinarySearch)
Two strings s and t of same length n are given. You can pick one character in s and another in t and swap them. Given you can make unlimited number of swaps, return whether it's possible to make the two strings equal.

xample :
Input:	s = "ab"	t = "ba"

Output: True


Approach:
We can only make one string into another when count of each character in both the strings combined is even.

For eg:
if we have 	s= 'abc' and  t= 'abd' converting one string to another is not possible as count of c and d is odd.

But if we had s='abcd' and t='cabd' then we could make them same by swapping. 

'''
s = 'abbbbbbbbb'
t = 'babbbbbbbb'

str1=s+t 
set1=set(str1) #to get only unique characters , no repetition 
for i in set1:
	if str1.count(i)%2!=0:
		return False
return True