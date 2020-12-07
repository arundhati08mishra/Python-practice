'''
Given a two-dimensional integer matrix, sort each of the columns in ascending order.

Approach:
Sorting rows is easier. So transpose the matrix, sort the rows, transpose again and return the matrix.
'''

def solve(matrix):
	return list(zip(*[list(sorted(i)) for i in zip(*matrix)])) # first transpose the matrix--> [list(i) for i in zip(*matrix)]
															   # sort the rows--> [list(sorted(i)) for i in zip(*matrix)]
															   # transpose again

m = [[10,20,30],[5,5,3],[0,10,7]]
print(solve(m))
