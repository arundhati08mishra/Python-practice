# ADD ONE (Binarysearch) Given a list of integers nums, representing a decimal number and nums[i] is between [0, 9].Return the same list in the same representation except modified so that 1 is added to the number.
#For eg: nums = [1,9,1]. o/p should be [1,9,2]
def solve(nums):
	str1='' 
	lst=[]
	for item in nums:
		str1+=str(item)	#store the elements in a list. [1,9,1] becomes '191'
	str2 = str(int(str1)+1) #convert str to int and add 1. Convert back to string so we can loop over elements.
	for i in str2:
		lst.append(int(i)) #[1,9,2]
	return(lst)

print(solve([1,9,1])) #test