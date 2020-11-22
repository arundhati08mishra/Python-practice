'''
Swap Consecutive Pair of Even Numbers ( problem from BinarySearch)
Given a list of integers nums, swap each consecutive even indexes with each other, and swap each consecutive odd indexes with each other.
ex:
i/p = nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
o/p = [2, 3, 0, 1, 6, 7, 4, 5, 8]
Explanation

0 and 2 gets swapped
1 and 3 gets swapped
4 and 6 gets swapped
5 and 7 gets swapped
8 remains the same

'''
def solve(nums):
        # Write your code here

        for i in range(0, len(nums)-2, 4): #swap even indices first. Start with 0th index. Every 4 indices, i is swapped with i+2. 
            nums[i],nums[i+2] = nums[i+2],nums[i] #swap

        for i in range(1,len(nums)-2,4): #swap odd indices. Start with 1st index.
            nums[i],nums[i+2] = nums[i+2],nums[i]
        return nums

print(solve([0,1,2,3,4,5,6,7,8]))