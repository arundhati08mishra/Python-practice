'''
Question: Given an integer n>=0, return whether it is a power of two.

Approach:
Keep on dividing the given integer by 2 till n>1. If 2 is left at the end it means n is a power of two.
'''

def power_two(n):
	if n==0:
		return False
	while n>1: 
		if n%2!=0 : #if n is an odd integer then False
			return False
		n=n/2 #keep on dividing by 2. And checking if the resultant n is not even. If odd then return False and end. If not odd then continue dividing by 2.
	return True 
print(power_two(32)) #check
print(power_two(9999)) #check