'''
Given an unsorted array of integers, sort the array into a wave like array. An array ‘arr[0..n-1]’ is sorted in wave 
form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..

Approach: Sort the array, then swap adjacent values.
Ex: input = [2,5,6,1,3,4]
sorted ==> [1,2,3,4,5,6] 
swap adjacent values: [2,1,4,3,6,5]

This satisfies the condition i.e., arr[0]>=arr[1]<=arr[2]>=arr[3].....
'''
def sortSwap(arr):
	arr.sort()
	for i in range(0, len(arr)-1,2):
		arr[i] , arr[i+1] = arr[i+1],arr[i]

	return arr
print(sortSwap([2,5,6,1,3,4])) 