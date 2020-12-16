'''
Question: Given a string s representing a number in base3, return its decimal integer equivalent.

Steps to convert from base3 to integer:
1) Multiply each digit with its corresponding power of three i.e. the right-most digit multiplied with (3**0) and so on.  
2) Add all of the numbers we get.

For detailed process see : https://www.geeksforgeeks.org/ternary-number-system-or-base-3-numbers/

Approach:
Starting from the right-most, we obtain each digit of the number: r = n%10.
And then divide the number by 10: n=n/10.
We multiply each digit with its corresponding power of three.


'''
def solve(s):
	i = 0
	r = 0
	num = 0
	n = int(s)
	while n!=0:
		r = n%10
		n = n//10
		num+= (r)* (3**i)
		i+=1
	return num
print(solve(10))