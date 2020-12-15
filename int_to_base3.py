'''
Question: Given an integer convert to base 3 representation and return as a string.

Approach:

Steps to Convert Decimal to Ternary:

1) We get the remainder r = n%3
2) Divide the number by 3
3) Repeat the steps until the quotient is equal to 0 and store the remainders

For detailed process see : https://www.geeksforgeeks.org/ternary-number-system-or-base-3-numbers/

Since we take the digits right-to-left so we need to reverse them when returning our final result.

Note: Handle negative numbers by considering its absolute(+ve) value and just appending '-' before the result. And for 0, result = 0.
'''
def solve(n):
	r=''
	if n < 0:
		return "-" + solve(abs(n)) #send the absolute value of n to the function and then append
	elif n == 0:
		return "0"
	else:
		while n:
			r+= str(n%3)
			n//=3
	return(r[::-1]) #reverse the result
print(solve(5))
print(solve(-27112727))